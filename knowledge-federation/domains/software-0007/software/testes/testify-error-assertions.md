---
id: software.testes.tranche17.001138
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
fontes: ["https://pkg.go.dev/github.com/stretchr/testify/assert", "https://pkg.go.dev/github.com/stretchr/testify/require"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Testify: verificar erros e tipos

## Em uma frase
Há funções específicas para confirmar que uma chamada devolve erro, que o erro é de determinado tipo ou que corresponde a um erro conhecido.

## Por que importa
Verificar apenas que existe erro aceita mensagens erradas, e a checagem por identidade garante que o caminho de erro previsto foi o executado.

## Como funciona
Verifique presença de erro, combine com a checagem de identidade ou tipo e evite comparar textos completos de mensagem.

## Exemplo
Uma função de domínio pode ser verificada quanto a devolver o erro sentinela definido quando o recurso não existe.

## Limites e trade-offs
Textos de mensagem mudam com frequência, e a comparação literal transforma refatoração de mensagens em falha de teste.

## Como verificar
Substitua o erro devolvido pelo serviço por outro tipo e confirme que a asserção correspondente passa a falhar.

## Conexões
- [[testify-equality-assertions]] — Veja também: Testify: comparar valores com clareza.
- [[testify-suite-lifecycle]] — Veja também: Testify: organizar casos em suítes.

## Fontes
- [Testify — Assert package](https://pkg.go.dev/github.com/stretchr/testify/assert) — asserções não fatais, comparadores e mensagens de falha; consultado em 2026-10-03.
- [Testify — Require package](https://pkg.go.dev/github.com/stretchr/testify/require) — asserções que interrompem o teste no primeiro erro; consultado em 2026-10-03.
