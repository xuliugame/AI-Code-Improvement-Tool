import { render, screen } from '@testing-library/react';
import App from '../src/App';

test('renders the main page', () => {
  render(<App />);
  expect(screen.getByText(/Code Improvement Tool/i)).toBeInTheDocument();
});
