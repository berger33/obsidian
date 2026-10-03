---
id: software.seguranca.tranche01.000024
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-01.md"
fontes: ["https://raw.githubusercontent.com/google/osv-scanner/main/README.md", "https://google.github.io/osv-scanner/usage/", "https://github.com/google/osv-scanner"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# OSV-Scanner Call Analysis (*Reachability*): análise de grafo de chamadas para verificar se a função vulnerável é realmente invocada

## Em uma frase
O OSV-Scanner suporta **Call Analysis (análise de alcançabilidade / *reachability*)** para ecossistemas suportados (como **Go** e **Rust**), construindo o grafo de chamadas do código-fonte da sua aplicação para determinar se a função ou símbolo específico afetado pela CVE é efetivamente chamado em algum caminho de execução.

## Por que importa
Frequentemente um projeto importa uma biblioteca grande apenas para usar uma função utilitária de formatação, enquanto uma CVE crítica é publicada em um parser XML da mesma biblioteca que nunca é importado nem chamado pelo seu código.

## Como funciona
Quando a análise de chamadas está ativa (`--call-analysis=go` / configuração de reachability), o OSV-Scanner classifica a vulnerabilidade como **Uncalled (não chamada)** se o símbolo vulnerável registrado no aviso OSV não for alcançável a partir do seu código, reduzindo drasticamente os alertas irrelevantes.

## Exemplo
```bash
# Executando o OSV-Scanner com análise de grafo de chamadas em um projeto Go:
osv-scanner scan source --call-analysis=go -r ./servico-go
```

## Limites e trade-offs
Mesmo quando uma vulnerabilidade é marcada como *uncalled* no momento atual, atualize a dependência no ciclo normal de manutenção para evitar que um PR futuro passe a chamar a função vulnerável.

## Como verificar
Inspecione a saída detalhada para distinguir vulnerabilidades alcançáveis (*called*) de vulnerabilidades não invocadas (*uncalled*).

## Conexões
- [[osvscanner-scan-image-containers-layer-aware-distros-artifacts]] — Veja também: OSV-Scanner `scan image`: varredura *layer-aware* de imagens de container (pacotes Alpine/Debian/Ubuntu e artefatos Go/Java/Node/Python).
- [[osvscanner-guided-remediation-fix-in-place-relax-override-pom-npm]] — Veja também: OSV-Scanner Guided Remediation (`osv-scanner fix`): estratégias `in-place`, `relax` e `override` para atualização segura de dependências.

## Fontes
- [Google OSV-Scanner GitHub — README.md (OSV-Scanner V2 Features, OSV-Scalibr Engine, Container Scanning, Call Analysis & Guided Remediation)](https://raw.githubusercontent.com/google/osv-scanner/main/README.md) — README oficial do google/osv-scanner descrevendo a arquitetura V2 baseada no OSV-Scalibr, suporte a lockfiles/SBOMs, imagens de container e remediação guiada; consultado em 2026-10-03.
- [OSV-Scanner Official Documentation — Usage & Configuration (scan source, scan image, fix Strategies, --licenses, Offline DB & osv-scanner.toml)](https://google.github.io/osv-scanner/usage/) — Documentação oficial de uso do OSV-Scanner detalhando flags de CLI, estratégias de osv-scanner fix (in-place, relax, override), auditoria SPDX e osv-scanner.toml; consultado em 2026-10-03.
- [Google OSV-Scanner — Official GitHub Repository](https://github.com/google/osv-scanner) — Repositório oficial Apache-2.0 do Google OSV-Scanner; consultado em 2026-10-03.
