---
id: software.testes.tranche16.001026
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-16.md"
fontes: ["https://github.com/pa11y/pa11y", "https://github.com/pa11y/pa11y-ci"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Pa11y: preparar a página com ações

## Em uma frase
Uma lista de ações executada antes da análise permite preencher campos, acionar botões e esperar mudanças de endereço, alcançando estados que exigem interação.

## Por que importa
Muitos problemas aparecem apenas depois da interação, e analisar a página inicial deixa esses estados sem verificação.

## Como funciona
Descreva as ações em sequência curta, termine com uma espera por condição observável e mantenha as credenciais fora do arquivo versionado.

## Exemplo
Um fluxo de acesso pode preencher usuário e senha, acionar o envio e aguardar a rota interna antes de a varredura começar.

## Limites e trade-offs
Ações frágeis quebram a varredura inteira quando o seletor muda, e a espera baseada em tempo fixo é menos confiável do que a espera por mudança de rota.

## Como verificar
Execute a varredura com e sem ações e confirme que os problemas encontrados na área autenticada aparecem apenas na execução preparada.

## Conexões
- [[pa11y-runners]] — Veja também: Pa11y: combinar motores de verificação.
- [[pa11y-reporters-and-exit]] — Veja também: Pa11y: escolher formato de saída e código de retorno.

## Fontes
- [Pa11y — repositório oficial](https://github.com/pa11y/pa11y) — linha de comando, padrões, motores, ações, relatórios e limites; consultado em 2026-10-03.
- [Pa11y CI — repositório oficial](https://github.com/pa11y/pa11y-ci) — varredura de múltiplas páginas, configuração e integração contínua; consultado em 2026-10-03.
