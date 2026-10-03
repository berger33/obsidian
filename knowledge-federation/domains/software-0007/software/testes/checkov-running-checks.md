---
id: software.testes.tranche19.001309
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-19.md"
fontes: ["https://github.com/bridgecrewio/checkov", "https://github.com/bridgecrewio/checkov/blob/master/README.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Checkov: selecionar e excluir verificações

## Em uma frase
A execução aceita lista de verificações a rodar, lista de exclusão e filtro por padrão de identificador.

## Por que importa
Selecionar um subconjunto permite adoção gradual, começando pelos riscos mais relevantes sem bloquear a esteira por todo o passivo.

## Como funciona
Comece pelas verificações de risco alto do projeto, documente as exclusões e reveja a lista a cada ciclo.

## Exemplo
Um projeto pode rodar apenas as verificações de criptografia e exposição pública enquanto organiza o restante.

## Limites e trade-offs
Excluir por padrão amplo esconde verificações novas que passariam a valer, e manter tudo ativo desde o início paralisa as entregas.

## Como verificar
Execute com a lista de exclusão e compare a contagem de achados com a execução completa para ver o que foi suprimido.

## Conexões
- [[checkov-frameworks]] — Veja também: Checkov: escolher a estrutura de infraestrutura analisada.
- [[checkov-suppressions]] — Veja também: Checkov: registrar supressões com justificativa.

## Fontes
- [Checkov — repositório oficial](https://github.com/bridgecrewio/checkov) — código-fonte, verificações e documentação do projeto; consultado em 2026-10-03.
- [Checkov — Guia de uso](https://github.com/bridgecrewio/checkov/blob/master/README.md) — execução, seleção de verificações, supressões, linha de base e segredos; consultado em 2026-10-03.
