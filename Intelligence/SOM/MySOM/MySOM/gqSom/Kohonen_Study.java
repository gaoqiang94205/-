package gqSom;

import java.util.List;
import java.util.Random;

public class Kohonen_Study {
	double[] inputlayer;
	double[] outlayer;
	double[][] weight_vocter;
	int number_ipt;
	int number_out;
	int epochs;
	int[] result;
	double learning_rate;
	int final_result = 0;

	public Kohonen_Study(int ipt, int out, int epochs) {
		this.number_ipt = ipt;
		this.number_out = out;
		this.epochs = epochs;
		this.result = new int[number_out];
	}
    
	void unify_deal(){
//		unify_tool(inputlayer);
		for(int i=0;i<number_out;i++){
			unify_tool(weight_vocter[i]);
		}
	}
	void unify_tool(double[] layer){
		double ipt_sum = 0;
		for(int j=0;j<number_ipt;j++){
			ipt_sum += Math.pow(layer[j],2);
		}
		ipt_sum = Math.sqrt(ipt_sum);
		for(int j=0;j<number_ipt;j++){
		    layer[j] = layer[j] / ipt_sum;
		}
	}
	public void initi() {
		int nb_ipt = this.number_ipt;
		int nb_out = this.number_out;
		this.learning_rate = 0.8;
//        this.inputlayer = ipt;
		Random ran = new Random();
		weight_vocter = new double[nb_out][nb_ipt];
		for (int i = 0; i < nb_out; i++)
			for (int j = 0; j < nb_ipt; j++) {
				weight_vocter[i][j] = ran.nextDouble();
			}
		this.unify_deal();
	}
	
    /**
     * @param ipt
     */
    void train(List<double[]> ipt){
    	int order = 0,a=0,b=0,c=0;
    //	while(a==b&&b==c&&a==c){
    	for(int num = 0;epochs>0;epochs--,num++){
    	  for(int j=0;j<ipt.size();j++){
    		this.setInputlayer(ipt.get(j));
    		this.unify_tool(inputlayer);
    	     order = this.find_winner();
    	    this.update_weight(order);
    	  }
    	  this.update_learnrate(num+1);
//    	  if(epochs % 3== 0){
//    		 order=(order+1)%3;
//    		 this.update_weight(order);
//    	  }  
       }
    	a = this.test1(ipt.get(0));
System.out.println(a);    	
  	    b = this.test1(ipt.get(5));
System.out.println(b);  	    
  	    c = this.test1(ipt.get(10));
System.out.println(c); 	    
     }
    
    public double[] getInputlayer() {
		return inputlayer;
	}

	public void setInputlayer(double[] inputlayer) {
		this.inputlayer = inputlayer;
	}

	int[] test(double[] data){
    	this.setInputlayer(data);
    	this.unify_tool(this.inputlayer);
    	this.cacu_result();
    	return this.result;
    }
	int test1(double[] data){
    	this.setInputlayer(data);
    	this.unify_tool(this.inputlayer);
    	this.cacu_result();
    	return this.final_result;
    }
	
    void cacu_result(){
    	int ord = this.find_winner();
    	int fina = 0;
    	for(int i=0,p=10;i<number_out;i++){
    		if(i==ord) {
    			result[i] = 1;
    			fina = fina*p + 1;
    		}
    		else{
    			this.result[i] = 0;
    			fina = fina*p + 0;
    		}
    	}
    	this.final_result = fina;
    }
	int find_winner() {
		int order = 0;
		double dis = cacu_distance(this.inputlayer, weight_vocter[0]);

		for (int n = 0; n < number_out; n++) {
			double dis_now = cacu_distance(inputlayer, weight_vocter[n]);
			if (dis > dis_now) {
				order = n;
				dis = dis_now;
			}
		}
		return order;
	}

	void update_weight(int order) {
		for (int i = 0; i < number_ipt; i++) {
			weight_vocter[order][i] = weight_vocter[order][i] - learning_rate * (inputlayer[i] - weight_vocter[order][i]);
		}
		this.unify_tool(weight_vocter[order]);
	}

	double cacu_distance(double[] ipt, double[] wstar) {
		double distance;
		double ipt_del_we = 0;

		for (int k = 0; k < number_ipt; k++) {
			ipt_del_we += Math.pow((ipt[k] - wstar[k]), 2);
		}
		distance = Math.sqrt(ipt_del_we);
		return distance;
	}

	void update_learnrate(int num) {
		double max = 0.8;
		learning_rate = max - num * (max / 10);
	}

}
