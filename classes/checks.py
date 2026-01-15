# classes/checks.py
class ResultChecker:
    def __init__(self, input_str):
        self.input = input_str.strip()  # Trim whitespace for checks

    def get_all_results(self):
        results = []
        results.append(f"Sisestatud: {self.input if self.input else '(tühi)'}\n")

        # String-based checks (always apply)
        results.append(f"Tühi või mitte: {'Tühi' if not self.input else 'Mitte tühi'}")

        starts_upper = 'Algab suure tähega' if self.input and self.input[
            0].isupper() else 'Ei alga suure tähega või tühi'
        results.append(f"Algab suure tähega või mitte: {starts_upper}")

        contains_digit = 'Sisaldab numbrit' if any(c.isdigit() for c in self.input) else 'Ei sisalda numbrit'
        results.append(f"Sisaldab numbrit või mitte: {contains_digit}")

        words = self.input.split()
        word_count = 'Üks sõna' if len(words) == 1 else f'Mitu sõna ({len(words)})' if len(
            words) > 1 else 'Ei sõnu (tühi)'
        results.append(f"Üks või mitu sõna: {word_count}")

        is_palindrome = 'Palindroom' if self.input and self.input.lower() == self.input.lower()[
            ::-1] else 'Ei ole palindroom või tühi'
        results.append(f"Palindroom või mitte: {is_palindrome}")

        # Number-based checks
        try:
            num = float(self.input)
        except ValueError:
            num_results = "Pole number"
            results.append(f"Paaris või paaritu: {num_results}")
            results.append(f"Positiivne või Negatiivne: {num_results}")
            results.append(f"Täisarv või Murdarv: {num_results}")
            results.append(f"Jagub kolmega või ei jagu kolmega: {num_results}")
            results.append(f"Ümmargune number või mitte: {num_results}")
        else:
            # Even or odd (only for integers)
            if num.is_integer():
                even_odd = "Paaris" if int(num) % 2 == 0 else "Paaritu"
            else:
                even_odd = "Pole täisarv"
            results.append(f"Paaris või paaritu: {even_odd}")

            # Positive or negative
            if num > 0:
                pos_neg = "Positiivne"
            elif num < 0:
                pos_neg = "Negatiivne"
            else:
                pos_neg = "Null"
            results.append(f"Positiivne või Negatiivne: {pos_neg}")

            # Integer or fractional
            int_frac = "Täisarv" if num.is_integer() else "Murdarv"
            results.append(f"Täisarv või Murdarv: {int_frac}")

            # Divisible by 3 (only for integers)
            if num.is_integer():
                div_three = "Jagub kolmega" if int(num) % 3 == 0 else "Ei jagu kolmega"
            else:
                div_three = "Pole täisarv"
            results.append(f"Jagub kolmega või ei jagu kolmega: {div_three}")

            # Round number (ends with 0 or 5, for integers)
            if num.is_integer():
                last_digit = str(int(num))[-1]
                round_num = "Ümmargune number" if last_digit in ('0', '5') else "Ei ole ümmargune number"
            else:
                round_num = "Pole täisarv"
            results.append(f"Ümmargune number või mitte: {round_num}")

        return "\n".join(results)