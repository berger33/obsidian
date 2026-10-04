---
id: software.testes.tranche20.001404
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
fontes: ["https://selenide.org/documentation/reports.html", "https://selenide.org/documentation/screenshots.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Selenide: registrar evidências e relatórios

## Em uma frase
A biblioteca captura telas em falhas e pode integrar-se a relatórios, com configuração por propriedades do projeto.

## Por que importa
A evidência no momento da falha encurta o diagnóstico, e o relatório consolida o resultado de toda a suíte.

## Como funciona
Ative a captura em falha, integre o ouvinte de relatório na preparação e publique o diretório de relatórios na esteira.

## Exemplo
A captura da tela no instante da falha mostra o estado que o teste observava, sem exigir reprodução local.

## Limites e trade-offs
Capturas em todas as execuções aumentam o volume sem acrescentar informação, e dados sensíveis visíveis na tela exigem tratamento antes da publicação.

## Como verificar
Provoque uma falha e confirme que a captura e o relatório referenciam o caso e o passo correspondentes.

## Conexões
- [[selenide-conditions]] — Veja também: Selenide: escolher condições de verificação.
- [[selenide-configuration]] — Veja também: Selenide: configurar navegador e limites.

## Fontes
- [Selenide — Relatórios](https://selenide.org/documentation/reports.html) — integração com relatórios de execução; consultado em 2026-10-03.
- [Selenide — Capturas de tela](https://selenide.org/documentation/screenshots.html) — captura automática em falhas e configuração; consultado em 2026-10-03.
