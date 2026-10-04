---
id: software.seguranca.tranche17.001660
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-17.md"
fontes: ["https://pnpm.io/cli/audit#--fix", "https://pnpm.io/settings/dependency-resolution#minimumreleaseage"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `minimumReleaseAge` e correções no pnpm: equilibrar atraso contra janela de ataque

## Em uma frase
Desde pnpm 11, `minimumReleaseAge` tem default documentado de 1.440 minutos (antes, zero); a janela pode atrasar releases, e `audit --fix` documenta uma exceção para a versão mínima corrigida.

## Por que importa
A janela reduz exposição a publicação recém-comprometida, mas pode atrasar uma correção urgente de vulnerabilidade se a policy não tratar exceções com cuidado.

## Como funciona
Defina o período com base no processo de resposta e revise as entradas automáticas em `minimumReleaseAgeExclude` quando a auditoria propõe uma versão de correção.

## Exemplo
Após um advisory de alta prioridade, revise o override e a exclusão temporal produzidos pela correção para confirmar que só a versão mínima necessária é liberada.

```text
pnpm audit --fix
```

## Limites e trade-offs
O default mudou no pnpm 11 e deve ser conferido na versão fixada; idade de release não verifica integridade ou qualidade, e um pacote malicioso pode permanecer publicado além da janela.

## Como verificar
Confira settings do workspace e diff de exclusões, instale em ambiente de teste e registre a aprovação explícita para a exceção de idade.

## Conexões
- [[pnpm-audit-signatures-registry-ecdsa-chaves]] — `pnpm audit signatures`: verificar assinaturas ECDSA do registry instalado.

## Fontes
- [pnpm — `audit --fix` e release-age](https://pnpm.io/cli/audit#--fix) — exceção necessária para instalar a versão mínima que corrige o advisory; consultado em 2026-10-04.
- [pnpm — `minimumReleaseAge`](https://pnpm.io/settings/dependency-resolution#minimumreleaseage) — default por versão, janela e exclusões temporais; consultado em 2026-10-04.
