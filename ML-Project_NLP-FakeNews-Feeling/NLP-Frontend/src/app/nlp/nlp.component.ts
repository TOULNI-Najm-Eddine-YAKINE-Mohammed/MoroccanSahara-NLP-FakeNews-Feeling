import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { NlpService } from '../nlpService/nlp.service';

@Component({
  selector: 'app-nlp',
  templateUrl: './nlp.component.html',
  styleUrls: ['./nlp.component.css']
})
export class NlpComponent implements OnInit {

  frm: boolean;
  frm1: boolean;
  frm2: boolean;
  alert: boolean;
  selectValue = 1;
  frmNbr = 0;
  message: any;

  constructor(
    private nlpService: NlpService
  ) { }

  ngOnInit(): void {
    this.frm = true;
    this.frm1 = false;
    this.frm2 = false;
    this.alert = false;
  }

  form00 = new FormGroup({
    text: new FormControl('', [
      Validators.required,
    ]),
  });

  form0 = new FormGroup({
    text: new FormControl('', [
      Validators.required,
    ]),
  });

  form = new FormGroup({
    text: new FormControl('', [
      Validators.required,
    ]),
  });

  form1 = new FormGroup({
    text: new FormControl('', [
      Validators.required,
    ]),
    nbr: new FormControl('', [
      Validators.required,
      Validators.pattern("^[0-9]*$"),
    ]),
  });

  form2 = new FormGroup({
    word1: new FormControl('', [
      Validators.required,
    ]),
    word2: new FormControl('', [
      Validators.required,
    ]),
  });

  nlpFunction(value){
    if(value == '3'){
      this.form1.setValue({'text':this.form.value['text'], 'nbr':null});
      this.frm1 = true;
      this.frm = false;
      this.frm2 = false;
    } else if (value == '11'){
      this.frm2 = true;
      this.frm = false;
      this.frm1 = false;
    } else {
      this.frm = true;
      this.frm1 = false;
      this.frm2 = false;
    }
    this.selectValue = Number(value);
  }

  submitFakeNews(){
    this.alert = true;
    this.nlpService.detectFakeNews(this.form0.value).subscribe(
      s=>{
        if(s['pClass'] == 0)
          this.message = 'this news is fake with a probability of : '+(s['probability'][0]*100).toFixed(2)+' %';
        else
          this.message = 'this news is real with a probability of : '+(s['probability'][1]*100).toFixed(2)+' %';
      },
      e=>{this.message = 'An Error Occurred';}
    );
  }

  submitSentiment(){
    this.alert = true;
    this.nlpService.feeling(this.form00.value).subscribe(
      s=>{
        if(s['feeling'][0]>0)
          this.message = 'Positive\nPolarity: ' + (100*s['feeling'][0]).toFixed(2) + '% Subjectivity: ' + (100*s['feeling'][1]).toFixed(2) + '%';
        else if(s['feeling'][0]<0)
          this.message = 'Negative\nPolarity: ' + (100*s['feeling'][0]).toFixed(2) + '% Subjectivity: ' + (100*s['feeling'][1]).toFixed(2) + '%';
        else
          this.message = 'Neutral'
      },
      e=>{this.message = 'An Error Occurred';}
    );
  }

  submitNLP(){
    this.alert = true;
    switch(this.selectValue){
      case 1: this.nlpService.tokenizationSentence(this.form.value).subscribe(
        s=>{
          var txt = '';
          s['sentences'].forEach(element => txt += element+'\n');
          this.message = txt;
        },
        e=>{this.message = 'An Error Occurred';}
      ); break;
      case 2: this.nlpService.tokenizationWord(this.form.value).subscribe(
        s=>{
          var txt = '';
          s['words'].forEach(element => txt += element+'\n');
          this.message = txt;
        },
        e=>{this.message = 'An Error Occurred';}
      ); break;
      case 3: this.nlpService.wordsFrequency(this.form1.value).subscribe(
        s=>{
          var txt = '';
          s['wordsFq'].forEach(element => txt += element+'\n');
          this.message = txt;
        },
        e=>{this.message = 'An Error Occurred';}
      ); break;
      case 4: this.nlpService.removePunctiation(this.form.value).subscribe(
        s=>{this.message = s['text'];},
        e=>{this.message = 'An Error Occurred';}
      ); break;
      case 5: this.nlpService.cleanText(this.form.value).subscribe(
        s=>{
          if (s['text'].length == 0)
            this.message = 'all these words are stop words';
          else
            this.message = s['text'];
        },
        e=>{this.message = 'An Error Occurred';}
      ); break;
      case 6: this.nlpService.stemming(this.form.value).subscribe(
        s=>{this.message = s['text'];},
        e=>{this.message = 'An Error Occurred';}
      ); break;
      case 7: this.nlpService.lemmatization(this.form.value).subscribe(
        s=>{this.message = s['text'];},
        e=>{this.message = 'An Error Occurred';}
      ); break;
      case 8: this.nlpService.posTagging(this.form.value).subscribe(
        s=>{
          var txt = '';
          s['tags'].forEach(element => txt += element+'\n');
          this.message = txt;
        },
        e=>{this.message = 'An Error Occurred';}
      ); break;
      case 9: this.nlpService.bagOfWords(this.form.value).subscribe(
        s=>{
          if(s['bagOfWords'].length > 0){
            var txt = '';
            s['bagOfWords'].forEach(element => txt += element+'\n');
            this.message = txt;
          }
          else
            this.message = 'you must write something about moroccan sahara';
        },
        e=>{this.message = 'An Error Occurred';}
      ); break;
      case 10: this.nlpService.tfidf(this.form.value).subscribe(
        s=>{
          if(s['tfidf'].length > 0){
            var txt = '';
            s['tfidf'].forEach(element => txt += element+'\n');
            this.message = txt;
          }
          else
            this.message = 'you must write something about moroccan sahara';
        },
        e=>{this.message = 'An Error Occurred';}
      ); break;
      case 11: this.nlpService.w2vSimilarity(this.form2.value).subscribe(
        s=>{this.message = 'similarity: '+(s['similarity']*100).toFixed(2)+' %';},
        e=>{this.message = 'you must write something about moroccan sahara';}
      ); break;
    }
  }
}
