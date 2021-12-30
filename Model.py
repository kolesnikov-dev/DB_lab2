import random
import Database
import time

Tables = {
    1: 'Products',
    2: 'Sellers',
    3: 'Clients',
    4: 'Prices',
    5: 'ClientsProducts',
    6: 'SellersProducts'
}

class Model:
    @staticmethod
    def existingtable(table):
        if str(table).isdigit():
             table = int(table)
             cons = True
             while cons:
                if table == 1 or table == 2 or table == 3 or table == 4 or table == 5 or table == 6:
                   return table
                else:
                   print('///Try again.')
                   return 0
        else:
             print('Try again')
             return 0


    @staticmethod
    def outputonetable(table):
        connect = Database.connect()
        cursor = connect.cursor()
        show = 'select * from public."{}"'.format(Tables[table])
        print("SQL query => ", show)
        print('')
        cursor.execute(show)
        datas = cursor.fetchall()
        cursor.close()
        Database.close(connect)
        return datas

    @staticmethod
    def insertProduct(f,s,added,notice):
        connect = Database.connect()
        cursor = connect.cursor()
        insert = 'DO $$ BEGIN if (1=1) and exists (select id from public."Prices" where id = {}) ' \
                 'then INSERT INTO public."Products"(name, PricesID, Prices) VALUES ({},{}); ' \
                 'raise notice {}; else raise notice {}; ' \
                 'end if; end $$;'.format(s, f, s, added, notice)
        cursor.execute(insert)
        connect.commit()
        print(connect.notices)
        cursor.close()
        Database.close(connect)

    @staticmethod
    def insertSeller(f, s, added, notice):
        connect = Database.connect()
        cursor = connect.cursor()
        insert = 'DO $$	BEGIN IF (1=1) THEN ' \
                 'INSERT INTO public."Sellers"(name, surname) values (\'{}\', \'{}\'); ' \
                 'RAISE NOTICE {};' \
                 ' ELSE RAISE NOTICE {};' \
                 'END IF; ' \
                 'END $$;'.format(f, s, added, notice)
        cursor.execute(insert)
        connect.commit()
        print(connect.notices)
        cursor.close()
        Database.close(connect)

    @staticmethod
    def insertClient(f,s,t,added,notice):
        connect = Database.connect()
        cursor = connect.cursor()
        insert = 'DO $$ BEGIN IF (1=1) THEN ' \
                 'INSERT INTO public."Clients"("Name", "Patronymic", "Surname") values ({}, {}, {}); ' \
                 'RAISE NOTICE {};' \
                 ' ELSE RAISE NOTICE {};' \
                 'END IF; ' \
                 'END $$;'.format(f,s,t, added, notice)
        cursor.execute(insert)
        connect.commit()
        print(connect.notices)
        cursor.close()
        Database.close(connect)

    @staticmethod
    def insertPrice(f,s,t,p,added,notice):
        connect = Database.connect()
        cursor = connect.cursor()
        insert = 'DO $$	BEGIN IF EXISTS (select "Id" from public."Clients" where "Id" = {}) and exists (select id from public."Sellers" where id = {}) THEN ' \
                 'INSERT INTO public."Prices"(time, ClientsID, SellersID, Price) values (\'{}\', {}, {},{}); ' \
                 'RAISE NOTICE {};' \
                 ' ELSE RAISE NOTICE {};' \
                 'END IF; ' \
                 'END $$;'.format(f, s, t, f, s,p, added, notice)
        cursor.execute(insert)
        connect.commit()
        print(connect.notices)
        cursor.close()
        Database.close(connect)

    @staticmethod
    def deleteProduct(idk, delete, notice):
        connect = Database.connect()
        cursor = connect.cursor()
        delete = 'DO $$ BEGIN IF EXISTS (select id from public."Products" where id = {}) then ' \
                 'delete from public."Prices" where id in (select PricesID from public."Products" where id = {});' \
                 'delete from public."Products" where id = {};' \
                 'raise notice {};' \
                 'else raise notice {};' \
                 'end if;' \
                 'end $$;'.format(idk, idk, idk, delete, notice)
        cursor.execute(delete)
        connect.commit()
        print(connect.notices)
        cursor.close()
        Database.close(connect)

    @staticmethod
    def deleteSellers(idk, delete, notice):
        connect = Database.connect()
        cursor = connect.cursor()
        delete = 'DO $$ BEGIN if ' \
                 'exists (select id from public."Sellers" where id = {}) then ' \
                 'delete from public."SellersProducts" where SellersID = {};' \
                 'delete from public."Prices" where SellersID = {};' \
                 'delete from public."Sellers" where id = {};' \
                 'raise notice {};' \
                 'else raise notice {};' \
                 'end if;' \
                 'end $$;'.format(idk, idk, idk, idk, delete, notice)
        cursor.execute(delete)
        connect.commit()
        print(connect.notices)
        cursor.close()
        Database.close(connect)

    @staticmethod
    def deleteClients(idk, delete, notice):
        connect = Database.connect()
        cursor = connect.cursor()
        delete = 'DO $$ BEGIN if ' \
                 'exists (select "Id" from public."Clients" where "Id" = {}) then ' \
                 'delete from public."ClientsProducts" where ClientsID = {};' \
                 'delete from public."Prices" where ClientsID = {};' \
                 'delete from public."Clients" where "Id" = {};' \
                 'raise notice {};' \
                 'else raise notice {};' \
                 'end if;' \
                 'end $$;'.format(idk, idk, idk, idk, delete, notice)
        cursor.execute(delete)
        connect.commit()
        print(connect.notices)
        cursor.close()
        Database.close(connect)

    @staticmethod
    def deletePrices(idk, delete, notice):
        connect = Database.connect()
        cursor = connect.cursor()
        delete = 'DO $$ BEGIN if exists (select id from public."Prices" where id = {}) then ' \
                 'delete from public."Prices" where id = {};' \
                 'raise notice {};' \
                 'else raise notice {};' \
                 'end if;' \
                 'end $$;'.format(idk, idk, delete, notice)
        cursor.execute(delete)
        connect.commit()
        print(connect.notices)
        cursor.close()
        Database.close(connect)

    @staticmethod
    def UpdateProduct(idk, name, updated, notice):
        connect = Database.connect()
        cursor = connect.cursor()
        update = 'DO $$ BEGIN IF EXISTS (select id from public."Products" where id = {}) THEN ' \
                 'update public."Products" set name = {} where id = {}; ' \
                 'RAISE NOTICE {};' \
                 ' ELSE RAISE NOTICE {};' \
                 'END IF; ' \
                 'END $$;'.format(idk, name, idk, updated, notice)
        cursor.execute(update)
        connect.commit()
        print(connect.notices)
        cursor.close()
        Database.close(connect)


    @staticmethod
    def UpdateSellers(idk, set1, set2, updated, notice):
        connect = Database.connect()
        cursor = connect.cursor()
        update = 'DO $$ BEGIN IF EXISTS (select id from public."Sellers" where id = {})' \
                 ' THEN ' \
                 'update public."Sellers" set Name = {}, Surname = {} where id = {}; ' \
                 'RAISE NOTICE {};' \
                 ' ELSE RAISE NOTICE {};' \
                 'END IF; ' \
                 'END $$;'.format(idk, set1, set2, idk, updated, notice)
        cursor.execute(update)
        connect.commit()
        print(connect.notices)
        cursor.close()
        Database.close(connect)

    @staticmethod
    def UpdateClients(idk, name, patronymic, surname, updated, notice):
        connect = Database.connect()
        cursor = connect.cursor()
        update = 'DO $$ BEGIN IF EXISTS (select "Id" from public."Clients" where "Id" = {}) ' \
                 ' THEN ' \
                 'update public."Clients" set "Name" = {}, "Patronymic" = {}, "Surname" = {} where "Id" = {}; ' \
                 'RAISE NOTICE {};' \
                 ' ELSE RAISE NOTICE {};' \
                 'END IF; ' \
                 'END $$;'.format(idk, name, patronymic, surname, idk, updated, notice)
        cursor.execute(update)
        connect.commit()
        print(connect.notices)
        cursor.close()
        Database.close(connect)

    @staticmethod
    def UpdatePrices(idk, date, updated, notice):
        connect = Database.connect()
        cursor = connect.cursor()
        update = 'DO $$ BEGIN IF EXISTS (select id from public."Prices" where id = {}) ' \
                 ' THEN ' \
                 'update public."Prices" set time = \'{}\' where id = {}; ' \
                 'RAISE NOTICE {};' \
                 ' ELSE RAISE NOTICE {};' \
                 'END IF; ' \
                 'END $$;'.format(idk, date, idk, updated, notice)
        cursor.execute(update)
        connect.commit()
        print(connect.notices)
        cursor.close()
        Database.close(connect)


    @staticmethod
    def selectionone(timestamp, SellerSurname):
        connect = Database.connect()
        cursor = connect.cursor()
        select = """
        select 
            public."Sellers".name, public."Sellers".surname, 
            public."Clients"."Name", public."Clients"."Surname"
            
            from public."Sellers"
            right join public."Prices" on public."Prices".Sellersid = public."Sellers".id
            left join public."Clients" on public."Prices".Clientsid = public."Clients"."Id"
            
            where public."Prices".time > '{}'
                and public."Sellers".surname like '{}'
        """.format(timestamp, SellerSurname)
        print("SQL query => ", select)
        beg = int(time.time() * 1000)
        cursor.execute(select)
        end = int(time.time() * 1000) - beg
        datas = cursor.fetchall()
        print('Time of request {} ms'.format(end))
        print('Selected')
        cursor.close()
        Database.close(connect)
        return datas

    @staticmethod
    def selectiontwo(subj, PriceTime):
        connect = Database.connect()
        cursor = connect.cursor()
        select = """
        select 
            public."Sellers".name, public."Sellers".surname, 
            public."Products".name,
            public."Prices".time
            
            from public."Products"
            join public."Prices"on public."Prices".id = public."Products".Pricesid
            join public."Sellers" on public."Prices".Sellersid = public."Sellers".id
            
            where public."Products".name like '{}'
                and public."Prices".time > '{}'
        """.format(subj, PriceTime)
        print("SQL query => ", select)
        beg = int(time.time() * 1000)
        cursor.execute(select)
        end = int(time.time() * 1000) - beg
        datas = cursor.fetchall()
        print('Time of request {} ms'.format(end))
        print('Selected')
        cursor.close()
        Database.close(connect)
        return datas

    @staticmethod
    def selectionthree(SellersS, ClientsS):
        connect = Database.connect()
        cursor = connect.cursor()
        select = """
        select public."Products".name from public."Products"

            join public."Prices"on public."Prices".id = public."Products".Pricesid
            
            join public."SellersProducts" 
                on public."SellersProducts".Productsid = public."Products".id
                and public."SellersProducts".Sellersid = public."Prices".Sellersid
            
            join public."ClientsProducts" 
                on public."ClientsProducts".Productsid = public."Products".id
                and public."ClientsProducts".Clientsid = public."Prices".Clientsid 
            
            join public."Clients" on "ClientsProducts".Clientsid = public."Clients"."Id"
            join public."Sellers" on public."SellersProducts".Sellersid = public."Sellers".id
                
            where public."Sellers".surname like '{}'
                and public."Clients"."Surname" like '{}'
                
            group by public."Products".name
        """.format(SellersS, ClientsS)
        print("SQL query => ", select)
        beg = int(time.time() * 1000)
        cursor.execute(select)
        end = int(time.time() * 1000) - beg
        datas = cursor.fetchall()
        print('Time of request {} ms'.format(end))
        print('Selected')
        cursor.close()
        Database.close(connect)
        return datas




    @staticmethod
    def randomik(table, kolvo):
            connect = Database.connect()
            cursor = connect.cursor()
            check = True
            while check:
                if table == 1:
                    res = 0
                    while (True):
                        insert = "INSERT INTO public.\"Products\"(Name, PricesID) select chr(trunc(65 + random()*26)::int)||chr(trunc(65 + r" \
                             "andom()*26)::int)," \
                             "(select id from public.\"Prices\" order by random() limit 1)" \
                             " from generate_series(1,{})".format(kolvo)
                        cursor.execute(insert)
                        res = res + 1
                        if(res == int(kolvo)):
                            break
                    check = False
                elif table == 2:
                    res = 0
                    while (True):
                        insert = "INSERT INTO public.\"Sellers\"(Name, Surname) select chr(trunc(65 + random()*26)::int)||chr(trunc(65 + r" \
                             "andom()*26)::int), " \
                             "chr(trunc(65 + random()*26)::int)||chr(trunc(65 + random()*26)::int) " \
                             "from generate_series(1,{})".format(kolvo)
                        cursor.execute(insert)
                        res = res + 1
                        if(res == int(kolvo)):
                            break
                    check = False
                elif table == 3:
                    res = 0
                    while (True):
                        insert = "INSERT INTO public.\"Clients\"(\"Name\", \"Surname\", \"Patronymic\") select chr(trunc(65 + random()*26)::int)||chr(trunc(65 + r" \
                             "andom()*26)::int), " \
                             "chr(trunc(65 + random()*26)::int)||chr(trunc(65 + random()*26)::int), " \
                             "chr(trunc(65 + random()*26)::int)||chr(trunc(65 + random()*26)::int)" \
                             "from generate_series(1,{})".format(kolvo)
                        cursor.execute(insert)
                        res = res + 1
                        if(res == int(kolvo)):
                            break
                    check = False
                elif table == 4:
                    res = 0
                    while (True):
                        insert = "INSERT INTO public.\"Prices\"(Time, ClientsID, SellersID) values(" \
                                 "(select NOW() + (random() * (NOW()+'90 days' - NOW())) + '{} days')," \
                                 "(select \"Id\" from public.\"Clients\" order by random() limit 1)," \
                                 "(select id from public.\"Sellers\" order by random() limit 1))".format(kolvo)
                        cursor.execute(insert)
                        res = res + 1
                        if (res == int(kolvo)):
                            break
                    check = False
                elif table == 5:
                    res = 0
                    while (True):
                        insert = "INSERT INTO public.\"ClientsProducts\"(ClientsID, ProductsID) values(" \
                                 "(select \"Id\" from public.\"Clients\" order by random() limit 1)," \
                                 "(select id from public.\"Products\" order by random() limit 1))".format(kolvo)
                        cursor.execute(insert)
                        res = res + 1
                        if (res == int(kolvo)):
                            break
                    check = False
                elif table == 6:
                    res = 0
                    while (True):
                        insert = "INSERT INTO public.\"SellersProducts\"(SellersID, ProductsID) values(" \
                                 "(select id from public.\"Sellers\" order by random() limit 1)," \
                                 "(select id from public.\"Products\" order by random() limit 1))".format(kolvo)
                        cursor.execute(insert)
                        res = res + 1
                        if (res == int(kolvo)):
                            break
                    check = False
            print(Tables[table])
            print("SQL query => ", insert)
            connect.commit()
            print('Inserted randomly')
            cursor.close()
            Database.close(connect)