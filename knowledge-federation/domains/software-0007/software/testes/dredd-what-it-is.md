---
id: software.testes.tranche25.001920
tipo: tecnica
dominio: software
subdominio: testes
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-25.md"
fontes: ["https://raw.githubusercontent.com/apiaryio/dredd/master/README.md", "https://github.com/apiaryio/dredd"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Dredd: validar o documento de descrição da API contra a implementação do backend

## Em uma frase
O README oficial define o Dredd como uma ferramenta de linha de comando agnóstica de linguagem para validar um documento de descrição de API contra a implementação de backend da API: ele lê a descrição da API e valida passo a passo se a implementação responde com as respostas descritas na documentação.

## Por que importa
Documentações de API escritas em arquivos separados do código tendem a apodrecer silenciosamente à medida que endpoints mudam; transformar o próprio documento de especificação na suíte de testes executável garante que qualquer divergência entre contrato documentado e resposta real quebre o build.

## Como funciona
Aponte o Dredd para o arquivo de descrição da API e para a URL do servidor da aplicação; para cada operação documentada, a ferramenta envia a requisição correspondente ao backend e compara status, cabeçalhos e corpo recebidos com o que o documento promete.

## Exemplo
Se a documentação diz que GET /messages retorna status 200 e um JSON com a chave message, o Dredd faz a chamada real ao backend e falha o passo se a implementação devolver outro código ou estrutura incompatível.

## Limites e trade-offs
O Dredd valida se as respostas reais obedecem aos exemplos e esquemas descritos no documento; ele não substitui testes unitários de regras de negócio internas nem testes exploratórios de segurança fora dos contratos documentados.

## Como verificar
Conferi o bloco de citação e o parágrafo introdutório no README oficial do repositório apiaryio/dredd.

## Conexões
- [[dredd-supported-api-description-formats]] — Veja também: Os três formatos de descrição de API: API Blueprint, OpenAPI 2 e OpenAPI 3 experimental.

## Fontes
- [Dredd — README oficial](https://raw.githubusercontent.com/apiaryio/dredd/master/README.md) — README oficial do Dredd com validação passo a passo de descrições de API (API Blueprint, OpenAPI 2 e OpenAPI 3 experimental) contra o backend, sete linguagens de hooks, instalação via npm e Quick Start com dredd init.; consultado em 2026-10-03.
- [Repositório oficial apiaryio/dredd](https://github.com/apiaryio/dredd) — Repositório oficial do Dredd no GitHub com código-fonte, releases e pipelines de CI.; consultado em 2026-10-03.
