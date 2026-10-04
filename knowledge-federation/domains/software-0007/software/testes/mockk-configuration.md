---
id: software.testes.tranche20.001425
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
fontes: ["https://github.com/mockk/mockk/blob/master/README.md", "https://github.com/mockk/mockk"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# MockK: configurar o comportamento padrão do projeto

## Em uma frase
Um arquivo de configuração permite definir relaxamento global, registro de chamadas privadas, relaxamento de funções sem retorno e classes que não podem ser dubladas.

## Por que importa
A configuração padroniza o comportamento entre casos e restringe a dublagem de tipos que não deveriam ser substituídos.

## Como funciona
Mantenha a configuração versionada, ative apenas as opções necessárias e liste expressamente as classes protegidas contra dublagem.

## Exemplo
O projeto pode relaxar funções sem retorno globalmente e impedir que tipos de valor ou classes do sistema sejam dublados.

## Limites e trade-offs
Relaxamento global esconde chamadas não configuradas, e listas de restrição desatualizadas deixam passar dublês indevidos.

## Como verificar
Duble temporariamente uma classe protegida e confirme que a configuração faz a execução falhar com mensagem clara.

## Conexões
- [[mockk-objects-and-statics]] — Veja também: MockK: dublar objetos e membros estáticos.
- [[mockk-relaxed-unit-and-defaults]] — Veja também: MockK: ajustar respostas padrão.

## Fontes
- [MockK — README oficial](https://github.com/mockk/mockk/blob/master/README.md) — dublês, relaxamento, verificação, objetos e corrotinas; consultado em 2026-10-03.
- [MockK — repositório oficial](https://github.com/mockk/mockk) — código-fonte, versões e documentação do projeto; consultado em 2026-10-03.
