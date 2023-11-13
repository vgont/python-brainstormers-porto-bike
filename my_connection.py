import oracledb as odb
from bicycle import Bicycle
from typing import List


class Connection:
    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.conn = None

    def __enter__(self):
        try:
            self.conn = odb.connect(user=self.user, password=self.password,
                                    dsn="oracle.fiap.com.br/orcl")
            return self.conn
        except Exception as e:
            print(e)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()

    def insert_new_bicycle(bicycle: dict):
        bike = Bicycle(bicycle)
        with Connection('rm98373', '120503') as conn:
            sql = f'''
                insert into t_cvb_bicicleta 
                (id_bicicleta, id_cliente, tp_uso_bicicleta, nr_serie_bicicleta, tipo_bicicleta, 
                nm_marca_bicicleta, nm_modelo_bicicleta, valor_bicicleta, categoria_bicicleta, nr_potencia_bicicleta) 
                values (SQ_T_CVB_BICICLETA.NEXTVAL,{bike.idClient}, {bike.age}, '{bike.serialNumber}', '{bike.type}', 
                '{bike.brand}', '{bike.model}', {bike.price}, 
                '{bike.category}', {verify_power_null(bike.powerInWatts)})
                '''

            cursor = conn.cursor()
            try:
                cursor.execute(sql)
                conn.commit()
            except Exception as e:
                print(f"Error occurred while inserting a new bicycle: {e}")

    def select_bikes_by_client_id(client_id: int) -> List[Bicycle] or None:
        sql = f"select * from t_cvb_bicicleta where id_cliente = {client_id}"
        with Connection('rm550657', '260305') as conn:
            cursor = conn.cursor()
            try:
                cursor.execute(sql)
                bicycles = []
                for row in cursor:
                    print(row)
                    bicycle_data = {
                        'idClient': row[1],
                        'age': row[2],
                        'serialNumber': row[3],
                        'type': row[4],
                        'brand': row[5],
                        'model': row[6],
                        'price': row[7],
                        'category': row[8],
                        'powerInWatts': row[9]
                    }

                    bicycles.append(bicycle_data)

                return bicycles
            except Exception as e:
                print(f"Error occurred while finding bikes: {e}")
                return None


def verify_power_null(power: float):
    if power is None:
        return 'null'
    return power
