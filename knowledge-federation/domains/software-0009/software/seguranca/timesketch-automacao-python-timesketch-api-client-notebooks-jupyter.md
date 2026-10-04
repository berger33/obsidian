---
id: software.seguranca.tranche06.000529
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-06.md"
fontes: ["https://raw.githubusercontent.com/google/timesketch/master/README.md", "https://timesketch.org/guides/user/sketch-overview/", "https://timesketch.org/guides/admin/install/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Timesketch: Ciência de Dados Forense com **`timesketch-api-client`**, DataFrames `pandas` e Container Jupyter Notebook (`picatrix`)

## Em uma frase
O pacote oficial **`timesketch-api-client`** (junto aos utilitários `picatrix` em containers JupyterLab integrados ao Timesketch) permite consultar qualquer Sketch programaticamente em Python e retornar os eventos diretamente como um **`pandas.DataFrame`** para análise estatística avançada.

## Por que importa
Detectar um *beaconing* de Comando e Controle com jitter aleatório (ex.: conexões a cada `300s ± 25%`) ou calcular o desvio padrão de bytes transferidos por hora exige funções estatísticas (`diff()`, `describe()`, FFT/autocorrelação) que são triviais em um DataFrame `pandas` mas difíceis em buscas textuais puras.

## Como funciona
O método `sketch.explore(query_string=..., return_fields=..., as_pandas=True)` executa a busca no OpenSearch e devolve o DataFrame tipado, permitindo também rotular, estrelar ou comentar eventos em lote de volta no Sketch após o processamento estatístico.

## Exemplo
```python
from timesketch_api_client import config

ts = config.get_client()
sketch = ts.get_sketch(42)

# Extrair eventos de rede como pandas DataFrame para analise estatistica de periodicidade de beaconing
df = sketch.explore(
    query_string='data_type:"zeek:conn" AND id_resp_p:443',
    return_fields="datetime,id_orig_h,id_resp_h,orig_bytes,resp_bytes",
    max_entries=10000,
    as_pandas=True
)
print(df["id_resp_h"].value_counts().head(10))
```

## Limites e trade-offs
Ao consultar timelines com milhões de linhas via `sketch.explore(..., as_pandas=True)`, passe sempre `return_fields` listando apenas as colunas necessárias e defina um `query_string` seletivo para evitar estourar a memória RAM do kernel Jupyter.

## Como verificar
Execute o script Python acima contra um sketch de homologação e confirme que `type(df)` é `pandas.core.frame.DataFrame` com as colunas solicitadas.

## Conexões
- [[timesketch-narrativa-forense-stories-grafos-relatorios-markdown]] — Veja também: Timesketch: Construção de Relatórios Forenses Reprodutíveis com **Stories**, Agregações Gráficas e Grafos de Relacionamento.
- [[timesketch-governanca-acls-protecao-delecao-arquivamento-tsctl]] — Veja também: Timesketch: Governança de Acesso (ACLs de Sketch), Rótulos de Preservação Legal (`protected` / `preserved`), Arquivamento e `tsctl`.
- [[timesketch-arquitetura-analise-colaborativa-timelines-forenses-opensearch]] — Referência cruzada direta com timesketch-arquitetura-analise-colaborativa-timelines-forenses-opensearch.
- [[timesketch-linguagem-busca-opensearch-dsl-saved-views-context-query]] — Referência cruzada direta com timesketch-linguagem-busca-opensearch-dsl-saved-views-context-query.

## Fontes
- [Google Timesketch Official GitHub — Collaborative Forensic Timeline Analysis](https://raw.githubusercontent.com/google/timesketch/master/README.md) — documentação oficial do Google Timesketch para análise colaborativa de timelines forenses; consultado em 2026-10-03.
- [Timesketch Official User Guide — Sketch Overview & Lifecycle](https://timesketch.org/guides/user/sketch-overview/) — guia oficial de abas do Sketch (Explore, Stories, Intelligence), tsctl, arquivamento e labels de proteção; consultado em 2026-10-03.
- [Timesketch Official Admin Guide — Installation & Configuration](https://timesketch.org/guides/admin/install/) — guia oficial de administração, Analyzers, Sigma e DFIQ no Timesketch; consultado em 2026-10-03.
