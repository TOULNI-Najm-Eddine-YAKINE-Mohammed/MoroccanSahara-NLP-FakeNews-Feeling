import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { NlpComponent } from './nlp/nlp.component';


const routes: Routes = [
  {path: '', redirectTo: 'nlp', pathMatch: 'full' },
  {path: 'nlp', component: NlpComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
