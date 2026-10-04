---
id: software.seguranca.tranche18.001775
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-18.md"
fontes: ["https://docs.github.com/en/code-security/getting-started/dependabot-quickstart-guide", "https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/secure-your-dependencies/configure-version-updates"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# GitHub Dependabot: Limitar pull requests em aberto

## Em uma frase
**GitHub Dependabot — Limitar pull requests em aberto:** A configuração pode limitar o número de PRs de atualização simultâneos por ecosystem.

## Por que importa
O recorte de **limitar pull requests em aberto** ajuda a expor dependências desatualizadas e vulneráveis e organizar mudanças verificáveis no repositório. A equipe registra risco, evidência e responsável.

## Como funciona
Para **limitar pull requests em aberto**, alertas dependem do grafo de dependências e updates são configurados em `dependabot.yml` por ecosystem, diretório e agenda. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Defina limite menor para um diretório legado que requer teste manual. Teste em staging autorizado.

## Limites e trade-offs
Limite zero desativa criação de updates naquele bloco e pode interromper resposta. Exceções exigem responsável e prazo.

## Como verificar
Inspecione configuração efetiva quando updates esperados não forem abertos. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[dependabot-ignorar-versoes-com-escopo]] — Complementa o tópico com github dependabot: ignorar versões com escopo.

## Fontes
- [GitHub Docs — Dependabot quickstart](https://docs.github.com/en/code-security/getting-started/dependabot-quickstart-guide) — guia oficial de alertas, security updates e version updates; consultado em 2026-10-04.
- [GitHub Docs — Configure version updates](https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/secure-your-dependencies/configure-version-updates) — referência oficial de formato `dependabot.yml`, ecosystems e schedules; consultado em 2026-10-04.
