#include <iostream>
#include <winsock.h>
using namespace std;

typedef class Relogio {
	private:
		bool ativo;
		int segundos;//0.60
		int min;//0.60
		int hora;
    public:
    	/* Prototipo vazio */
		Relogio(): segundos(0), ativo(false){
		}
		/* Prototipo que ja inicializa */
    	Relogio(int seg){
    		iniciar(seg);
		}
		
		/* Adiciona ciclo de segundo */
		void ciclo(){
			if(!ativo){
				cout << "Relogio inativo!" << endl;
				return;
			}
			
			if(segundos+1 >= 60){
				segundos=0;
				min++;
			}
			else segundos+=1;
			
			if(min >= 60){
				segundos = 0;
				min = 0;
				hora++;
			}
			
		}
		
    	/* Inicia em 'seg' */
    	void iniciar(int seg){
			segundos = seg;
			ativo = true;
		}
		
    	/* Reseta 'seg' e pausa */
		void parar(){
			segundos = 0;
			ativo = false;
		}
		
    	/* ... */
		void pausar(){
			ativo = !ativo;
		}
		
		/* Imprimir o relogio */
		void mostrar(){
			cout << "Timer: "<< hora << 
					":"		 << min << 
					":" 	 << segundos << endl;
		}

}Relogio;

int main(){
	Relogio *rel = new Relogio(0);
	while(1){
		system("cls");
		rel->ciclo();
		rel->mostrar();
		Sleep(1000);
	}
}