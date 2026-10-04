---
id: software.testes.tranche20.001419
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
fontes: ["https://github.com/mockk/mockk/blob/master/README.md", "https://github.com/mockk/mockk"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# MockK: criar dublês e definir respostas

## Em uma frase
A biblioteca cria dublês de tipos Kotlin e define o comportamento esperado em blocos que descrevem a chamada e o valor devolvido.

## Por que importa
A sintaxe em bloco reutiliza a própria expressão de chamada como chave, evitando cadeias de configuração verbosas.

## Como funciona
Crie o dublê, configure apenas as chamadas usadas pelo caso e mantenha o bloco próximo do uso correspondente.

## Exemplo
O dublê do repositório pode devolver o usuário esperado na consulta por identificador, mantendo as demais chamadas sem configuração.

## Limites e trade-offs
Configurar chamadas que o caso não usa adiciona ruído e mascara dependências não declaradas do código sob teste.

## Como verificar
Remova uma configuração usada pelo código e confirme que a execução falha apontando a chamada sem resposta definida.

## Conexões
- [[mockk-strict-vs-relaxed]] — Veja também: MockK: escolher entre modo estrito e relaxado.

## Fontes
- [MockK — README oficial](https://github.com/mockk/mockk/blob/master/README.md) — dublês, relaxamento, verificação, objetos e corrotinas; consultado em 2026-10-03.
- [MockK — repositório oficial](https://github.com/mockk/mockk) — código-fonte, versões e documentação do projeto; consultado em 2026-10-03.
