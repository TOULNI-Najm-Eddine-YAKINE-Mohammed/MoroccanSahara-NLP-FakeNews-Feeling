import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class NlpService {

  private url = 'http://127.0.0.1:5000';

  constructor(
    private http: HttpClient,
  ) { }

  tokenizationSentence(text: any):any {
    return this.http.post(`${this.url}/tokenizationSentence`, text);
  }

  tokenizationWord(text:any):any {
    return this.http.post(`${this.url}/tokenizationWord`, text);
  }

  wordsFrequency(textAndNbr:any):any {
    return this.http.post(`${this.url}/wordsFrequency`, textAndNbr);
  }

  removePunctiation(text:any):any {
    return this.http.post(`${this.url}/removePunctiation`, text);
  }

  cleanText(text:any):any {
    return this.http.post(`${this.url}/cleanText`, text);
  }

  stemming(text:any):any {
    return this.http.post(`${this.url}/stemming`, text);
  }

  lemmatization(text:any):any {
    return this.http.post(`${this.url}/lemmatization`, text);
  }

  posTagging(text:any):any {
    return this.http.post(`${this.url}/posTagging`, text);
  }

  bagOfWords(text:any):any {
    return this.http.post(`${this.url}/bagOfWords`, text);
  }

  tfidf(text:any):any {
    return this.http.post(`${this.url}/tfidf`, text);
  }

  w2vSimilarity(word1AndWord2:any):any {
    return this.http.post(`${this.url}/w2vSimilarity`, word1AndWord2);
  }

  detectFakeNews(text:any):any {
    return this.http.post(`${this.url}/detectFakeNews`, text);
  }

  feeling(text:any):any {
    return this.http.post(`${this.url}/feeling`, text);
  }

}
