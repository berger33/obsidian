---
id: software.testes.tranche17.001107
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
fontes: ["https://github.com/appium/appium", "https://appium.io/docs/en/latest/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Appium: entender a arquitetura de drivers

## Em uma frase
O servidor é extensível, e cada plataforma é suportada por um driver instalado separadamente, com a automação escolhida por capacidade.

## Por que importa
A separação permite atualizar o suporte a uma plataforma sem alterar o núcleo e deixa explícito qual componente executa cada comando.

## Como funciona
Instale apenas os drivers necessários, fixe versões e declare a automação correspondente na capacidade de cada execução.

## Exemplo
Uma equipe que automatiza Android e iOS instala os dois drivers e escolhe o adequado conforme o alvo da execução.

## Limites e trade-offs
Drivers ausentes produzem erro na criação da sessão, e versões incompatíveis entre servidor e driver geram falhas de comando difíceis de diagnosticar.

## Como verificar
Liste os drivers instalados e confirme que a sessão de teste usa exatamente o driver esperado para a plataforma indicada.

## Conexões
- [[appium-capabilities]] — Veja também: Appium: declarar capacidades da sessão.
- [[appium-locator-strategies]] — Veja também: Appium: escolher seletores móveis.

## Fontes
- [Appium — repositório oficial](https://github.com/appium/appium) — arquitetura de drivers e plugins, CLI de extensões e servidor; consultado em 2026-10-03.
- [Appium — Documentation](https://appium.io/docs/en/latest/) — capacidades, drivers, seletores, gestos e contexto de sessão; consultado em 2026-10-03.
