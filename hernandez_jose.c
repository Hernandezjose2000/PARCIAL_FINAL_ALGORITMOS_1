#include <stdio.h>


const int MAXIMA = 100;


void mostrar_vector_minimo_maximo(int array[], int longitud_vector){


    int ingresar_valores = 0;
    for(ingresar_valores;ingresar_valores<longitud_vector;ingresar_valores++){
        printf("Ingrese un valor por favor ");
        scanf(" %d", &array[ingresar_valores]);

    }

    int iterador = 0;
    for(iterador;iterador<longitud_vector;iterador++){
        int iterador_auxiliar = 0;
        for(iterador_auxiliar;iterador_auxiliar<longitud_vector -1; iterador_auxiliar++){
            if(array[iterador_auxiliar]>array[iterador_auxiliar+1]){
                int valor_auxiliar = array[iterador_auxiliar];
                array[iterador_auxiliar] = array[iterador_auxiliar+1];
                array[iterador_auxiliar+1] = valor_auxiliar;
            }
        }
    }

    iterador = 0;
    printf("El vector [");
    for(iterador;iterador<longitud_vector;iterador++){
        printf(" %d", array[iterador]);
    }
    printf("] tiene como maximo al %d y como minimo al %d\n", array[longitud_vector-1], array[0]);
}


int main(){

    int longitud_vector = 0;
    printf("Por favor ingrese la cantidad de numeros a ingresar no debe ser mayor a 100\n");
    scanf(" %d", &longitud_vector);
    while(longitud_vector>100){
        printf("Has superado la cantidad maxima que es100. Intenta nuevamente por faovr\n");
        scanf(" %d", &longitud_vector);
    }
    int array[MAXIMA];
    mostrar_vector_minimo_maximo(array,longitud_vector);
    return 0;
}
