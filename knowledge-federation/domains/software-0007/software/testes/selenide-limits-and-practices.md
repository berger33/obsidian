---
id: software.testes.tranche20.001408
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
fontes: ["https://selenide.org/documentation.html", "https://github.com/selenide/selenide"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Selenide: reconhecer limites

## Em uma frase
A biblioteca simplifica a escrita de testes de interface sobre a interface de navegador, sem substituir testes de unidade, de integração nem de desempenho.

## Por que importa
Suítes de interface são lentas e frágeis por natureza, e concentrar nelas toda a verificação alonga a esteira sem medir a lógica interna.

## Como funciona
Reserve a suíte de interface para os fluxos críticos, prefira seletores estáveis e mantenha as regras detalhadas nas camadas inferiores.

## Exemplo
O cálculo de frete pertence ao teste de unidade, enquanto a jornada de compra com pagamento pertence à suíte de interface.

## Limites e trade-offs
Mesmo com esperas automáticas, alterações de layout e ambiente continuam exigindo manutenção; a cobertura de interface não mede comportamento sob carga.

## Como verificar
Escolha uma falha recorrente e avalie se ela pertence à camada de interface ou poderia ser detectada mais cedo por teste de unidade.

## Conexões
- [[selenide-migration-from-selenium]] — Veja também: Selenide: migrar de código Selenium direto.

## Fontes
- [Selenide — Documentação](https://selenide.org/documentation.html) — API de elementos, coleções, condições e esperas automáticas; consultado em 2026-10-03.
- [Selenide — repositório oficial](https://github.com/selenide/selenide) — código-fonte, versões e documentação do projeto; consultado em 2026-10-03.
