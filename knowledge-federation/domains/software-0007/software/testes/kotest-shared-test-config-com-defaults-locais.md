---
id: software.testes.tranche15.000905
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: "2026-10-02"
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://kotest.io/docs/framework/sharedtestconfig.html", "https://kotest.io/docs/framework/project-config.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Kotest 6.2: centralizar defaults sem impedir ajustes por caso

## Em uma frase
`DefaultTestConfig` compartilha opções entre casos de uma spec e permite que configuração direta de um teste tenha precedência sobre defaults herdados.

## Por que importa
Centralizar timeouts, ordem, assertion mode, retries ou coroutine test scope reduz duplicação, mas um valor global excessivo pode mudar silenciosamente a semântica de todos os casos.

## Como funciona
Configuração deve se manter próxima do grupo cujo contrato ela descreve.

## Exemplo
Defina defaults no início de uma Spec e marque explicitamente o timeout maior apenas no teste que espera uma operação lenta, em vez de aumentar todo o projeto.

## Limites e trade-offs
Configuração compartilhada não é a mesma coisa que configuração do engine inteiro; algumas opções de execução só podem ser definidas no nível do projeto.

## Como verificar
Inspecione a configuração efetiva de um caso padrão e outro sobrescrito, além de conferir a saída de config dump quando a precedência não estiver clara.

## Conexões
- [[kotest-retries-com-delay-na-configuracao-compartilhada]] — Veja também: Kotest 6.2: configurar retries sem apagar o sinal de falha intermitente.
- [[kotest-prepare-spec-e-instancias-recriadas]] — Veja também: Kotest 6.2: escolher listener de setup conforme o número de instâncias.

## Fontes
- [Kotest 6.2 — Shared Test Config](https://kotest.io/docs/framework/sharedtestconfig.html) — defaults de teste, timeout, retry e precedência local; consultado em 2026-10-02.
- [Kotest 6.2 — Project Level Config](https://kotest.io/docs/framework/project-config.html) — configuração de engine no nível do projeto e precedência; consultado em 2026-10-02.
