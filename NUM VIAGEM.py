import pandas as pd

planilha = r'Planilha Entrada'
df_deslocamento = pd.read_excel(planilha, sheet_name='DESLOCAMENTO')

df_deslocamento['QUE HORAS INICIOU O DESLOCAMENTO'] = pd.to_datetime(df_deslocamento['QUE HORAS INICIOU O DESLOCAMENTO'])

df_deslocamento_sorted = df_deslocamento.sort_values(by=['ID DOMICÍLIO', 'QUE HORAS INICIOU O DESLOCAMENTO'])

df_deslocamento_sorted['NUM_VIAGEM'] = df_deslocamento_sorted.groupby('ID DOMICÍLIO').cumcount() + 1

df_deslocamento_sorted['VIAGENS_TOTAIS'] = df_deslocamento_sorted.groupby('ID DOMICÍLIO')['NUM_VIAGEM'].transform('max')

duplicated_mask = df_deslocamento_sorted.duplicated(subset='ID DOMICÍLIO', keep='first')

df_deslocamento_sorted.loc[~duplicated_mask, 'VIAGENS_TOTAIS'] = df_deslocamento_sorted['VIAGENS_TOTAIS'].astype('Int64')
df_deslocamento_sorted.loc[duplicated_mask, 'VIAGENS_TOTAIS'] = '--'

output_file = r'Planilha saída'
df_deslocamento_sorted.to_excel(output_file, index=False)
