#include <iostream>
using namespace std;
int harga,jumlahtiket,totalharga,tambahan,totaltambahan,total,hargaakhir,diskon,potongan;
string tujuan,kelas;
int main(){
    cout<<endl<<"Nama : Salsabilla Tri Putri";
    cout<<endl<<"NIM  : 2310431017";
    cout<<endl;
    cout<<endl<<"BUS PT.ANS LINTAS SUMATERA";
    cout<<endl;
    cout<<endl<<"------------------------------";
    cout<<endl<<" NO   TUJUAN      HARGA TIKET";
    cout<<endl<<"------------------------------";
    cout<<endl<<" 1.  Surabaya     Rp1.100.000";
    cout<<endl<<" 2.  Jakarta      Rp600.000";
    cout<<endl<<" 3.  Bandung      Rp700.000";
    cout<<endl<<" 4.  Depok        Rp650.000";
    cout<<endl<<" 5.  Bogor        Rp650.000";
    cout<<endl<<" 6.  Tangerang    Rp670.000";
    cout<<endl<<"------------------------------";
    cout<<endl;
    cout<<" Tujuan        : ";cin>>tujuan;

    if(tujuan == "Surabaya") {harga = 1100000;
    }  else {if(tujuan == "Jakarta") {harga = 600000 ;}
            else {if(tujuan == "Bandung") {harga = 700000;}
                else {if(tujuan == "Depok") {harga = 650000;}
                    else {if(tujuan == "Bogor") {harga = 650000;}
                        else {if(tujuan == "Tangerang") {harga = 670000;}
                            else {harga = 0;}}}}}}

    cout<<endl;
    cout<<endl<<"--------------------------------------";
    cout<<endl<<" NO        KELAS        BIAYA TAMBAHAN";
    cout<<endl<<"--------------------------------------";
    cout<<endl<<" 1.    Economic Class      Rp10.000";
    cout<<endl<<" 2.    Business Class      Rp20.000";
    cout<<endl<<" 3.    First Class         Rp30.000";
    cout<<endl<<"--------------------------------------";
    cout<<endl<<" Kelas                : ";cin>>kelas;
    cout<<" Jumlah tiket         : ";cin>>jumlahtiket;
    cout<<" Harga tiket          : "<<harga;
    totalharga = harga*jumlahtiket;
    cout<<endl<<" Total harga tiket    : "<<totalharga;
    if (kelas == "Economic"){tambahan = 10000;
    }   else {if(kelas == "Business"){tambahan = 20000;}
             else {if(kelas == "FirstClass"){tambahan = 30000;}
                  else {tambahan = 0;}}}
    cout<<endl<<" Tambahan biaya       : "<<tambahan;
    totaltambahan = tambahan*jumlahtiket;
    cout<<endl<<" Total biaya tambahan : "<<totaltambahan;
    cout<<endl;
    cout<<endl<<"-----------------";
    cout<<endl<<" RINCIAN PESANAN";
    cout<<endl<<"-----------------";
    cout<<endl<<" Tujuan       : "<<tujuan;
    cout<<endl<<" Kelas        : "<<kelas;
    cout<<endl<<" Jumlah tiket : "<<jumlahtiket;
    total = totalharga+totaltambahan;
    cout<<endl<<" Total harga  : "<<total;
    if (jumlahtiket>=3 && jumlahtiket<=5) {diskon = 5;
    }   else {if(jumlahtiket>5) {diskon = 10;}
            else {diskon = 0;}}
    potongan = 0.01*diskon*total;
    cout<<endl<<" Diskon       : "<<potongan;
    hargaakhir = total-potongan;
    cout<<endl<<" Harga akhir  : "<<hargaakhir;
    cout<<endl;
}
