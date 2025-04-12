import pandas
import pandas as pd


csv = pandas.read_csv('ibmEmployeeDomain - performanceRating.csv')

#VERIFICANDO ERROS NA TABELA 'performanceRating' NA COLUNA 'EmployeeNumber'


def verify_employee():
    try:
        int_employee = pd.to_numeric(csv['EmployeeNumber'], errors='coerce').astype('Int64')
        failed_conversions = csv[
            int_employee.isna() &
            csv['EmployeeNumber'].notna()
            ]
        problematic_values = failed_conversions['EmployeeNumber']
        print(f"Valores que não puderam ser convertidos ({len(failed_conversions)} encontrados):")
        print(failed_conversions)
        failed_conversions['ConversionError'] = 'Valor não numérico'
        failed_conversions.to_csv('problemas_employee.csv', index=False)
    except Exception as e:
        print(f"Erro de conversão {e}")

#VERIFICANDO ERROS NA TABELA 'performanceRating' NA COLUNA 'EmployeeNumber'


def verify_performance():
    try:
        int_performance = pd.to_numeric(csv['PerformanceRating'], errors='coerce').astype('Int64')
        conversion_fails = csv[
            int_performance.isna() &
            csv['PerformanceRating'].notna()
            ].copy()
        conversion_fails['ErrorType'] = 'Não numérico'
        null_values = csv[csv['PerformanceRating'].isna()].copy()
        null_values['ErrorType'] = 'Valor NULL'
        all_issues = pd.concat([conversion_fails, null_values])
        print(f"Total de problemas: {len(all_issues)}")
        print(all_issues[['PerformanceRating', 'ErrorType']])

        all_issues.to_csv('problemas_performance.csv', index=False)

        return all_issues
    except Exception as e:
        print(f"Erro de conversão {e}")

verify_employee()
verify_performance()