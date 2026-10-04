---
id: software.testes.tranche16.001020
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
fontes: ["https://googlechrome.github.io/lighthouse-ci/docs/configuration.html", "https://github.com/GoogleChrome/lighthouse-ci"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Lighthouse CI: versionar a configuração

## Em uma frase
A configuração pode ficar em arquivo JavaScript, JSON ou YAML, com seções para coleta, verificação, publicação, servidor e assistente.

## Por que importa
Arquivo versionado garante que execução local e pipeline usem as mesmas regras e que mudanças passem por revisão.

## Como funciona
Mantenha um único arquivo na raiz, organize por seção e use caminho explícito para configuração alternativa quando o pipeline exigir.

## Exemplo
Um mesmo arquivo pode listar páginas, desligar auditorias específicas e declarar o destino de publicação usado por todos os ambientes.

## Limites e trade-offs
Múltiplos arquivos com nomes parecidos criam dúvida sobre qual está ativo, e sobrescrever a configuração por linha de comando esconde o que realmente foi aplicado.

## Como verificar
Renomeie temporariamente o arquivo e observe o comportamento da execução para confirmar de onde as opções estão sendo lidas.

## Conexões
- [[lighthouseci-upload-targets]] — Veja também: Lighthouse CI: escolher destino dos resultados.
- [[lighthouseci-artifacts-and-reports]] — Veja também: Lighthouse CI: consumir resultados e relatórios locais.

## Fontes
- [Lighthouse CI — Configuration](https://googlechrome.github.io/lighthouse-ci/docs/configuration.html) — seções collect, assert e upload, presets, asserções e orçamentos; consultado em 2026-10-03.
- [Lighthouse CI — repositório oficial](https://github.com/GoogleChrome/lighthouse-ci) — comandos, integração contínua e documentação do projeto; consultado em 2026-10-03.
