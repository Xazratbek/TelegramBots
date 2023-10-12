from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool
from data import config
from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

DB_USER = env.str("DB_USER")
DB_PASS = env.str("DB_PASS")
DB_NAME = env.str("DB_NAME")
DB_HOST = env.str("DB_HOST")


class Database:

    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database=config.DB_NAME,
        )

    async def execute(self, command, *args,
                      fetch: bool = False,
                      fetchval: bool = False,
                      fetchrow: bool = False,
                      execute: bool = False
                      ):
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    async def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS foydalanuvchilar (
        id SERIAL PRIMARY KEY,
        first_name varchar(255) NULL,
        last_name varchar(500) NULL,
        username varchar(255) NULL,
        telegram_id BIGINT NOT NULL UNIQUE,
        is_active INT default 1
        );
        """
        await self.execute(sql, execute=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ${num}" for num, item in enumerate(parameters.keys(),
                                                          start=1)
        ])
        return sql, tuple(parameters.values())

    async def add_user(self, first_name, last_name, username, telegram_id, is_active):
        sql = f"INSERT INTO foydalanuvchilar (first_name, last_name,username, telegram_id, is_active) VALUES('{first_name}','{last_name}','{username}','{telegram_id}', '{is_active}');"
        return await self.execute(sql, fetchrow=True)

    async def user_exists(self, telegram_id):
        sql = f"SELECT * FROM foydalanuvchilar WHERE telegram_id='{telegram_id}';"
        data = await self.execute(sql, fetch=True)
        return bool(len(data))

    async def set_active(self, telegram_id, active):
        sql = f"UPDATE foydalanuvchilar SET is_active='{active}' WHERE telegram_id='{telegram_id}';"
        return await self.execute(sql, execute=True)

    async def select_count_active_users(self):
        sql = f"SELECT COUNT(*) FROM foydalanuvchilar WHERE is_active=1;"

        return await self.execute(sql, fetchval=True)

    async def select_all_users(self):
        sql = "SELECT * FROM foydalanuvchilar;"
        return await self.execute(sql, fetch=True)

    async def select_user(self, **kwargs):
        sql = "SELECT * FROM foydalanuvchilar WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)

    async def count_users(self):
        sql = "SELECT COUNT(*) FROM foydalanuvchilar"
        return await self.execute(sql, fetchval=True)

    async def update_user_username(self, username, telegram_id):
        sql = "UPDATE foydalanuvchilar SET username=$1 WHERE telegram_id=$2"
        return await self.execute(sql, username, telegram_id, execute=True)

    async def delete_users(self):
        await self.execute("DELETE FROM foydalanuvchilar WHERE TRUE", execute=True)

    async def drop_users(self):
        await self.execute("DROP TABLE foydalanuvchilar", execute=True)