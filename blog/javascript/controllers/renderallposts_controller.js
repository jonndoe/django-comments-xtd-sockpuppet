import { Controller } from 'stimulus';
import StimulusReflex from 'stimulus_reflex';

export default class extends Controller {
  connect() {
    StimulusReflex.register(this)
  }

  increment(event) {
    console.log('increment')
    event.preventDefault()
    this.stimulate('renderallpostsReflex#increment', 1)
  }

  render(event) {
    console.log('render')
    event.preventDefault()
    this.stimulate('renderallpostsReflex#render')
  }

  renderfrompaginator(event) {
    console.log('renderfrompaginator')
    event.preventDefault()
    this.stimulate('renderallpostsReflex#renderfrompaginator')
  }


}
