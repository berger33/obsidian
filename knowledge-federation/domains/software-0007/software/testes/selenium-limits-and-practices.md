---
id: software.testes.tranche17.001105
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
fontes: ["https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/", "https://www.selenium.dev/documentation/webdriver/waits/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Selenium: reconhecer limites e boas práticas

## Em uma frase
O driver automatiza o navegador, mas não valida conteúdo, desempenho nem acessibilidade, e a suíte precisa ser combinada com outras verificações.

## Por que importa
Esperar que a suíte de interface cubra todos os níveis produz execuções lentas, frágeis e com baixa capacidade de localizar defeitos.

## Como funciona
Reserve testes de interface para fluxos críticos, cubra a lógica em níveis inferiores e mantenha a suíte pequena e estável o suficiente para rodar em cada revisão.

## Exemplo
Regras de cálculo e validação de formulário pertencem a testes de unidade, enquanto a interface verifica que o fluxo principal permanece funcionando.

## Limites e trade-offs
Duplicar em interface o que já é verificado em nível inferior aumenta o tempo do pipeline sem ganho proporcional de confiança.

## Como verificar
Selecione um caso de interface e verifique se o mesmo defeito seria detectado por um teste de unidade existente antes de manter a duplicação.

## Conexões
- [[selenium-flakiness-diagnosis]] — Veja também: Selenium: diagnosticar instabilidade.

## Fontes
- [Selenium — Page object models](https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/) — objetos de página e de componente e boas práticas de estruturação; consultado em 2026-10-03.
- [Selenium — Waits](https://www.selenium.dev/documentation/webdriver/waits/) — espera implícita e explícita por condições observáveis; consultado em 2026-10-03.
