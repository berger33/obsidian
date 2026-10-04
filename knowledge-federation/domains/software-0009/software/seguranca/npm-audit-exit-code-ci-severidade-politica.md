---
id: software.seguranca.tranche17.001650
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
fontes: ["https://docs.npmjs.com/cli/v11/commands/npm-audit#description", "https://docs.npmjs.com/cli/v11/using-npm/config#audit-level"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Códigos de saída do `npm audit`: transformar achados em política CI explícita

## Em uma frase
Por padrão, o npm retorna código diferente de zero quando encontra vulnerabilidades; o limiar pode ser alterado por `audit-level`.

## Por que importa
A CI precisa comunicar claramente se falhou por vulnerabilidade, falha de rede ou erro de configuração, sem converter indisponibilidade de registry em sucesso silencioso.

## Como funciona
Preserve exit codes, publique relatório em qualquer resultado e combine threshold com monitoramento de erro de serviço para manter o gate observável.

## Exemplo
O job pode executar auditoria, armazenar JSON e marcar o build como falho se o nível configurado for atingido ou se a consulta não puder ser concluída.

```text
npm audit --audit-level=high
```

## Limites e trade-offs
Um único código não oferece triagem completa; scripts que ignoram falhas ou substituem o status podem ocultar resultados reais.

## Como verificar
Teste cenários limpo, vulnerável e registry indisponível e confirme que cada caso produz status e mensagem distintos no pipeline.

## Conexões
- [[npm-audit-signatures-provenance-attestations-distincao]] — `npm audit signatures`: verificação separada de assinatura e proveniência do registry.

## Fontes
- [npm CLI v11 — `npm audit`](https://docs.npmjs.com/cli/v11/commands/npm-audit#description) — exit status padrão, erro de consulta e relatório de vulnerabilidades; consultado em 2026-10-04.
- [npm CLI v11 — configuração `audit-level`](https://docs.npmjs.com/cli/v11/using-npm/config#audit-level) — threshold configurável para falha da auditoria; consultado em 2026-10-04.
