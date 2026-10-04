---
id: software.testes.tranche17.001142
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
fontes: ["https://pkg.go.dev/github.com/stretchr/testify/mock", "https://github.com/stretchr/testify"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Testify: gerar dublês a partir de interfaces

## Em uma frase
A geração automática produz implementações de dublê a partir das interfaces do projeto, mantendo o código de apoio sincronizado com as assinaturas.

## Por que importa
Dublês escritos à mão envelhecem quando a interface muda, e o gerador transforma a mudança em falha de compilação em vez de teste silencioso.

## Como funciona
Gere os dublês a partir das interfaces, versione os arquivos gerados e regenere quando a assinatura mudar.

## Exemplo
Uma interface de notificação pode ter dublê regenerado após ganhar um novo método, forçando a atualização dos casos que a usam.

## Limites e trade-offs
Arquivos gerados precisam ser regenerados na versão do gerador fixada pelo projeto, e a mistura de manual com gerado cria confusão.

## Como verificar
Altere a assinatura de um método da interface, regenere e confirme que os casos que não atualizam a expectativa deixam de compilar ou falhar.

## Conexões
- [[testify-mock-argument-matchers]] — Veja também: Testify: casar argumentos de forma flexível.
- [[testify-http-testing]] — Veja também: Testify: apoiar testes de HTTP.

## Fontes
- [Testify — Mock package](https://pkg.go.dev/github.com/stretchr/testify/mock) — expectativas de chamada, correspondência de argumentos e verificação final; consultado em 2026-10-03.
- [Testify — repositório oficial](https://github.com/stretchr/testify) — código-fonte, exemplos e documentação do projeto; consultado em 2026-10-03.
