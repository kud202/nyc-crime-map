
def main():
    for table_id, select in [
         ('02378420399528461352-17772055697785505571', 'YR,MO,geometry,X,Y,TOT,CR'),
         ('02378420399528461352-11853667273131550346', 'YR,MO,geometry,X,Y,TOT'),
    ]:
        head(table_id, select)
        to_csv(table_id, select)
        to_geojson(table_id, select)

if __name__ == '__main__':
    main()
