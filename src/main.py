from importData import load_housing_data

def main():
    housing = load_housing_data()
    print(housing.head())

if __name__=="__main__":
    main()