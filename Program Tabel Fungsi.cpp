
#include <iostream>
#include <cmath>
using namespace std;

const int MAX_DATA = 100;

int main() {
    string nama = "  Salsabilla Tri Putri";
    string nim = "  2310431017";
    string shift = "  2";

    cout << endl;
    cout << "  TUGAS 5 PRAKTIKUM ADP\n" << endl;
    cout << "  Materi : ARRAY" << endl;
    cout << "  Nama   : " << nama << endl;
    cout << "  NIM    : " << nim << endl;
    cout << "  Shift  : " << shift << endl;
    cout << endl;

    while (true) {
        int n;
        cout << "  Banyak data : ";
        cin >> n;

        if (n > MAX_DATA) {
            cout << "  Jumlah data melebihi batas maksimum." << endl;
            continue;
        }

        int x[MAX_DATA], fx[MAX_DATA], gx[MAX_DATA], hx[MAX_DATA];

        for (int i = 0; i < n; ++i) {
            cout << "  Nilai x ke-" << i+1 << " : ";
            cin >> x[i];
            if (x[i] > 0) {
                fx[i] = 3*x[i]*x[i] + 7*x[i] - 2;
            } else if (x[i] < 0) {
                fx[i] = 2*x[i]*x[i] - 5*x[i] - 4;
            } else {
                fx[i] = 0;
            }
            gx[i] = fx[i]*fx[i] - sqrt(fx[i]);
            hx[i] = fx[i] * gx[i];
        }

        cout << "\n   --------------------------------------------------" << endl;
        cout << "  |                   TABEL HASIL                    |" << endl;
        cout << "  |--------------------------------------------------|" << endl;
        cout << "  |    x    |    f(x)    |    g(x)    |     h(x)     |" << endl;
        cout << "  |--------------------------------------------------|" << endl;
        for (int i = 0; i < n; ++i) {
            cout << "  |    " << x[i] << "   |     " << fx[i] << "    |   " << gx[i] << "   |   " << hx[i] << "  |" << endl;
        }
        cout << "   -------------------------------------------------- " << endl;
        cout << endl;

        char pilihan;
        cout << "  Apakah Anda ingin kembali memasukkan nilai x ? (Y/N): ";
        cin >> pilihan;
        if (pilihan != 'Y' && pilihan != 'y') {
            break;
        }
    }
}
