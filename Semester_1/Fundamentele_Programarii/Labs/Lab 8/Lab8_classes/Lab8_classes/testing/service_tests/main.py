from business.service_clients import ServiceClients
from business.service_movies import ServiceMovies
from business.service_rentals import ServiceRentals
from domain.domain_client import Client
from errors.repo_error import RepoError
from infrastuctura.repo_client import RepoClient
from infrastuctura.repo_movie import RepoMovie
from infrastuctura.repo_rentals import RepoRentals
from validation.validate_client import ValidatingClient
from validation.validate_movie import ValidatingMovie
from validation.validate_rentals import ValidatingRentals


class Serv_tests:
    def __init__(self):
        pass
    def service_tests(self):
        self.serv_test_c()
        self.serv_test_m()
        self.serv_test_r()
    def serv_test_c(self):
        self.addc()
        self.sec()
    def serv_test_m(self):
        self.addm()
        self.sem()

    def serv_test_r(self):
        self.addr()
        self.modr()

    def addc(self):
        rtc = RepoClient()
        vtc=ValidatingClient()
        stc=ServiceClients(vtc,rtc)
        id = 25
        name = "Do I work"
        CNP = "2880918378050"
        st=stc.add_client(id,name,CNP)
        assert st.get_id_client()==id
        assert st.get_name_client()==name
        assert st.get_CNP_client()==CNP
    def sec(self):
        rtc = RepoClient()
        vtc = ValidatingClient()
        stc = ServiceClients(vtc, rtc)
        id = 25
        name = "Do I work"
        CNP = "2880918378050"
        try:
            stc.search_client_by_id(id)
            assert False
        except RepoError:
            pass
        st = stc.add_client(id, name, CNP)
        s_f=stc.search_client_by_id(id)
        assert st==s_f
        #linked to serv_m
    def addm(self):
        rtm = RepoMovie()
        vtm = ValidatingMovie()
        stm = ServiceMovies(vtm, rtm)
        id = 25
        name = "Do I work"
        genre="romance"
        description="i exist man"
        st = stm.add_movie(id, name, genre,description)
        assert st.get_id_movie() == id
        assert st.get_name_movie() == name
        assert st.get_genre_movie() == genre
        assert st.get_description_movie() == description
    def sem(self):
        rtm = RepoMovie()
        vtm = ValidatingMovie()
        stm = ServiceMovies(vtm, rtm)
        id = 25
        name = "Do I work"
        genre = "romance"
        description = "i exist man"
        try:
            stm.search_movie_by_id(id)
        except RepoError:
            pass
        st = stm.add_movie(id, name, genre, description)
        st_r=stm.search_movie_by_id(id)
        assert st==st_r
    #linked to rentals
    def addr(self):
        rtm = RepoMovie()
        vtm = ValidatingMovie()
        stm = ServiceMovies(vtm, rtm)
        rtc = RepoClient()
        vtc = ValidatingClient()
        stc = ServiceClients(vtc, rtc)
        rtr=RepoRentals()
        vtr=ValidatingRentals()
        str=ServiceRentals(vtr,rtr,rtc,rtm,vtc,vtm)
        client=stc.random_client_generator()
        id_m = 25
        name_m = "Do I work"
        genre_m = "romance"
        description_m = "i exist man"
        movie = stm.add_movie(id_m, name_m, genre_m, description_m)
        idr=21
        d=23
        rental=str.add_rental(idr,client.get_id_client(),movie.get_id_movie(),d)
        assert rental.get_id_rental()==idr
        assert rental.get_days_rental()==d
        assert rental.get_movie()==movie
        assert rental.get_client()==client
    def modr(self):
        rtm = RepoMovie()
        vtm = ValidatingMovie()
        stm = ServiceMovies(vtm, rtm)
        rtc = RepoClient()
        vtc = ValidatingClient()
        stc = ServiceClients(vtc, rtc)
        rtr = RepoRentals()
        vtr = ValidatingRentals()
        str = ServiceRentals(vtr, rtr, rtc, rtm, vtc, vtm)
        client = stc.random_client_generator()
        id_m = 25
        name_m = "Do I work"
        genre_m = "romance"
        description_m = "i exist man"
        movie = stm.add_movie(id_m, name_m, genre_m, description_m)
        idr = 21
        d = 23
        try:
            str.search_rental(idr)
            assert False
        except RepoError:
            pass
        rental = str.add_rental(idr, client.get_id_client(), movie.get_id_movie(), d)
        assert rental==str.search_rental(idr)



