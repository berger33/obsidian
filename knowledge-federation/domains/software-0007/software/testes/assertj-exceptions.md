---
id: software.testes.tranche20.001415
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-20.md"
fontes: ["https://assertj.github.io/doc/", "https://github.com/assertj/assertj"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# AssertJ: verificar exceções

## Em uma frase
As asserções de exceção verificam tipo, mensagem, causa e presença de trechos na mensagem, sem captura manual de try e catch.

## Por que importa
A verificação dirigida de exceção confirma o contrato de erro sem inflar o teste com código de captura.

## Como funciona
Encadeie a asserção de lançamento com a verificação do tipo e da mensagem, e verifique a causa quando o contrato exigir.

## Exemplo
O teste pode exigir que a operação lance erro de validação com a mensagem indicando o campo obrigatório.

## Limites e trade-offs
Verificar apenas o tipo de exceção deixa passar mensagens que perderam a informação de contexto para o usuário.

## Como verificar
Faça a operação deixar de lançar a exceção e confirme que a mensagem de falha registra a ausência do lançamento esperado.

## Conexões
- [[assertj-custom-assertions]] — Veja também: AssertJ: criar asserções próprias de domínio.
- [[assertj-recursive-and-fields]] — Veja também: AssertJ: comparar campos e estruturas.

## Fontes
- [AssertJ — Documentação](https://assertj.github.io/doc/) — asserções fluentes, coleções, descrições, asserções suaves e próprias; consultado em 2026-10-03.
- [AssertJ — repositório oficial](https://github.com/assertj/assertj) — código-fonte, versões e documentação do projeto; consultado em 2026-10-03.
