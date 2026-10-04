---
id: software.seguranca.tranche18.001790
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
fontes: ["https://github.com/CycloneDX/cyclonedx-cli", "https://github.com/CycloneDX/specification/blob/master/schema/bom-1.7.schema.json"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# CycloneDX CLI: Interpretar BOM como inventário, não scan

## Em uma frase
**CycloneDX CLI — Interpretar BOM como inventário, não scan:** BOM descreve componentes e dados declarados, mas a CLI não decide se uma vulnerabilidade é explorável.

## Por que importa
O recorte de **interpretar bom como inventário, não scan** ajuda a manipular SBOMs CycloneDX com verificações repetíveis em fluxos de build e auditoria. A equipe registra risco, evidência e responsável.

## Como funciona
Para **interpretar bom como inventário, não scan**, a CLI lê um BOM e um formato declarado, executa uma operação específica e emite resultado ou novo documento. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Passe BOM validado a scanner de vulnerabilidade como entrada separada do build. Teste em staging autorizado.

## Limites e trade-offs
Ausência de finding em análise de BOM não prova que a imagem esteja livre de falhas. Exceções exigem responsável e prazo.

## Como verificar
Compare inventário com imagem e rode ferramenta de vulnerabilidade sobre o digest exato. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[cfn-guard-modelar-uma-clause-booleana]] — Complementa o tópico com aws cloudformation guard: modelar uma clause booleana.

## Fontes
- [CycloneDX CLI — Repository and commands](https://github.com/CycloneDX/cyclonedx-cli) — documentação oficial de analyze, convert, diff, merge, sign, verify e validate; consultado em 2026-10-04.
- [CycloneDX specification — BOM 1.7 schema](https://github.com/CycloneDX/specification/blob/master/schema/bom-1.7.schema.json) — schema oficial usado para validar estrutura de BOM CycloneDX 1.7; consultado em 2026-10-04.
