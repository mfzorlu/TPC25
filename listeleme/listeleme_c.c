#include <stdio.h>
#include <stdlib.h>

int max_in_window(int *arr, int start, int length) {
    int max_val = arr[start];
    for (int i = start + 1; i < start + length; i++) {
        if (arr[i] > max_val) {
            max_val = arr[i];
        }
    }
    return max_val;
}

int min_in_array(int *arr, int length) {
    int min_val = arr[0];
    for (int i = 1; i < length; i++) {
        if (arr[i] < min_val) {
            min_val = arr[i];
        }
    }
    return min_val;
}

int main() {
    int adet;
    scanf("%d", &adet);

    int *puanlar = (int *)malloc(adet * sizeof(int));
    for (int i = 0; i < adet; i++) {
        scanf("%d", &puanlar[i]);
    }

    int *sonuc = (int *)malloc(adet * sizeof(int));

    for (int grupUzunlugu = 1; grupUzunlugu <= adet; grupUzunlugu++) {
        int max_listesi_length = adet - grupUzunlugu + 1;
        int *max_listesi = (int *)malloc(max_listesi_length * sizeof(int));

        for (int baslangicDegeri = 0; baslangicDegeri < max_listesi_length; baslangicDegeri++) {
            max_listesi[baslangicDegeri] = max_in_window(puanlar, baslangicDegeri, grupUzunlugu);
        }

        sonuc[grupUzunlugu - 1] = min_in_array(max_listesi, max_listesi_length);
        free(max_listesi);
    }

    for (int i = 0; i < adet; i++) {
        printf("%d\n", sonuc[i]);
    }

    free(puanlar);
    free(sonuc);

    return 0;
}
