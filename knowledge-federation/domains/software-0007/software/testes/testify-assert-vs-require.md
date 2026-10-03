---
id: software.testes.tranche17.001136
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-17.md"
fontes: ["https://pkg.go.dev/github.com/stretchr/testify/assert", "https://github.com/stretchr/testify"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Testify: distinguir asserção de verificação fatal

## Em uma frase
O pacote de asserção registra a falha e continua a execução, enquanto o pacote equivalente interrompe o teste no primeiro erro.

## Por que importa
Continuar após uma condição essencial violada produz uma cascata de erros falsos que esconde a causa real da falha.

## Como funciona
Use a variante fatal para pré-condições das quais o restante do teste depende e a variante comum para verificações independentes.

## Exemplo
Se a criação de um recurso falha, a verificação fatal interrompe o caso, evitando que o teste siga usando um identificador vazio.

## Limites e trade-offs
Interromper cedo demais esconde outras divergências do mesmo caso, e o uso indiscriminado da variante fatal reduz a informação disponível.

## Como verificar
Provoque uma falha em pré-condição de um caso com várias verificações e confirme que o relatório interrompe no ponto correto, sem erros derivados.

## Conexões
- [[testify-equality-assertions]] — Veja também: Testify: comparar valores com clareza.

## Fontes
- [Testify — Assert package](https://pkg.go.dev/github.com/stretchr/testify/assert) — asserções não fatais, comparadores e mensagens de falha; consultado em 2026-10-03.
- [Testify — repositório oficial](https://github.com/stretchr/testify) — código-fonte, exemplos e documentação do projeto; consultado em 2026-10-03.
