---
id: software.testes.tranche12.000609
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
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-12.md"
fontes: ["https://docs.phpunit.de/en/12.5/risky-tests.html", "https://docs.phpunit.de/en/12.5/xml-configuration-file.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# PHPUnit 12.5: classificar tamanhos e limites de duração

## Em uma frase
Atributos Small, Medium e Large classificam testes por custo e permitem aplicar limites temporais correspondentes na configuração.

## Por que importa
Uma taxonomia consistente distingue feedback rápido de integração demorada e ajuda a escolher quando incluir grupos maiores em cada etapa.

## Como funciona
Atribua o tamanho pelo recurso usado e duração observada, configure limites no XML e trate um teste que excede orçamento como investigação, não como convite automático para elevar todos os limites.

## Exemplo
Uma verificação pura pode pertencer ao grupo pequeno, enquanto um fluxo que sobe serviços externos recebe classificação maior e roda em job apropriado.

## Limites e trade-offs
Limites de tempo dependem do ambiente e podem marcar testes como risky quando ultrapassados; tamanho declarado não é garantia de que o caso seja independente.

## Como verificar
Compare duração real com o limite no runner de CI e confirme que job rápido não executa inadvertidamente a categoria de custo maior.

## Conexões
- [[phpunit-risky-output-assertions]] — Veja também: PHPUnit 12.5: interpretar testes marcados como risky.

## Fontes
- [PHPUnit 12.5 — Risky Tests](https://docs.phpunit.de/en/12.5/risky-tests.html) — testes sem assertions, output e critérios de risco; consultado em 2026-10-02.
- [PHPUnit 12.5 — XML Configuration](https://docs.phpunit.de/en/12.5/xml-configuration-file.html) — configuração de grupos, isolamento, execução e resultado; consultado em 2026-10-02.
