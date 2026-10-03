---
id: software.testes.tranche21.001465
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-21.md"
fontes: ["https://nightwatchjs.org/guide/reference/settings.html", "https://github.com/nightwatchjs/nightwatch"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Nightwatch: página de objetos pelo caminho

## Em uma frase
A chave page_objects_path aponta as pastas de onde os objetos de página são carregados e ficam disponíveis pelo namespace page da API do teste.

## Por que importa
Centralizar seletores e trechos de navegação por página evita repetir localizadores frágeis em todos os arquivos de teste da suíte.

## Como funciona
Descreva cada tela em um arquivo próprio, registre o caminho na configuração e acesse o objeto pelo cliente para expor elementos e ações da área.

## Exemplo
O objeto da página de login pode expor o campo de usuário, a senha e um método entrar, reutilizados por qualquer teste de autenticação.

## Limites e trade-offs
Página objetos viram um segundo framework quando acumulam asserções de negócio; mantenha a decisão de teste no arquivo de teste.

## Como verificar
Liste as páginas carregadas a partir do caminho configurado e confirme que o namespace page resolve o nome de cada arquivo.

## Conexões
- [[nightwatch-capabilities-desired]] — Veja também: Nightwatch: desiredCapabilities e sessões.
- [[nightwatch-custom-commands-assertions]] — Veja também: Nightwatch: estender com comandos e asserções próprios.

## Fontes
- [Nightwatch — Referência de Config Settings](https://nightwatchjs.org/guide/reference/settings.html) — chaves de configuração, ambientes, runner, workers e capturas; consultado em 2026-10-03.
- [Nightwatch — repositório oficial](https://github.com/nightwatchjs/nightwatch) — código-fonte, releases e documentação do projeto; consultado em 2026-10-03.
