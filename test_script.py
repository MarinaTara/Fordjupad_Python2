from sqlalchemy import create_engine
import pandas as pd
import pytest

# test database connection
def test_db_conn():
	try:
		engine = create_engine('mssql+pyodbc://MARINA/ExampleDatabase?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server')
		connection = engine.connect()
		connection.close()
		assert True	 # Test passes if no exception is raised
	except Exception:
		assert False # Test fails if an exception occurs
				
# test if SQL table exists
def test_table_exists():
    try:
        engine = create_engine('mssql+pyodbc://MARINA/ExampleDatabase?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server')
        query = "SELECT 1 FROM dbo.Customer"
        df = pd.read_sql(query, engine)
        assert not df.empty # test passes if data exists
    except Exception:
        assert False # test fails if table missing
        
        
# test data processing
def test_data_process():
    test_data = pd.DataFrame({'LastName': ['davidsson', 'johnsson', 'johansson']})
    test_data["LastName"] = test_data["LastName"].str.upper()
    assert all(test_data["LastName"] == ['DAVIDSSON', 'JOHNSSON', 'JOHANSSON'])
    
if __name__ == "__main__":
    pytest.main()
