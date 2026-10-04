---
id: software.seguranca.tranche18.001788
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

# CycloneDX CLI: Escolher versão de saída conscientemente

## Em uma frase
**CycloneDX CLI — Escolher versão de saída conscientemente:** Opções de versão permitem converter para versões CycloneDX aceitas pelo consumidor.

## Por que importa
O recorte de **escolher versão de saída conscientemente** ajuda a manipular SBOMs CycloneDX com verificações repetíveis em fluxos de build e auditoria. A equipe registra risco, evidência e responsável.

## Como funciona
Para **escolher versão de saída conscientemente**, a CLI lê um BOM e um formato declarado, executa uma operação específica e emite resultado ou novo documento. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Emita a versão exigida pela plataforma downstream e registre-a como parte do contrato. Teste em staging autorizado.

## Limites e trade-offs
Consumidor antigo pode rejeitar campos novos; especificação nova pode mudar estrutura. Exceções exigem responsável e prazo.

## Como verificar
Execute validação no produtor e no consumidor de teste com a mesma versão declarada. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[cyclonedx-cli-integrar-validacao-ao-ci]] — Complementa o tópico com cyclonedx cli: integrar validação ao ci.

## Fontes
- [CycloneDX CLI — Repository and commands](https://github.com/CycloneDX/cyclonedx-cli) — documentação oficial de analyze, convert, diff, merge, sign, verify e validate; consultado em 2026-10-04.
- [CycloneDX specification — BOM 1.7 schema](https://github.com/CycloneDX/specification/blob/master/schema/bom-1.7.schema.json) — schema oficial usado para validar estrutura de BOM CycloneDX 1.7; consultado em 2026-10-04.
