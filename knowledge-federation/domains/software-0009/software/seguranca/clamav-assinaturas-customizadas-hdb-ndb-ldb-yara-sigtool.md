---
id: software.seguranca.tranche04.000315
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-04.md"
fontes: ["https://raw.githubusercontent.com/Cisco-Talos/clamav/main/README.md", "https://docs.clamav.net/manual/Usage.html", "https://docs.clamav.net/manual/Signatures.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# ClamAV: Escrita de Assinaturas Customizadas (`.hdb`, `.hsb`, `.ndb`, `.ldb`, `.yar`) e `sigtool`

## Em uma frase
O ClamAV suporta múltiplos formatos de assinaturas locais em `/var/lib/clamav/`: hashes de arquivo (`.hdb`/`.hsb`), assinaturas de bytes com offset e wildcards (`.ndb`), expressões lógicas combinadas (`.ldb`) e regras YARA (`.yar`).

## Por que importa
Permite às equipes de resposta a incidentes bloquear instantaneamente novas variantes de malware, anexos de phishing específicos da organização ou binários comprometidos antes da publicação nas bases globais.

## Como funciona
O utilitário `sigtool` gera assinaturas de hash (`sigtool --md5` / `--sha256` salvos em `.hsb`), converte strings em hexadecimal (`sigtool --hex-dump`) e descompacta bancos `.cvd` para auditoria (`sigtool --unpack`). Já as assinaturas lógicas `.ldb` combinam múltiplas sub-assinaturas com operadores booleanos, contadores de ocorrência e restrições de tipo de alvo (`Target:1` para PE, `Target:0` para qualquer arquivo).

## Exemplo
```bash
# Gerar assinatura SHA-256 (.hsb) de um binário malicioso coletado pelo SOC
sigtool --sha256 /tmp/sample-dropper.bin > /var/lib/clamav/soc-custom-ioc.hsb

# Testar a nova assinatura diretamente contra a amostra usando clamscan -d
clamscan -d /var/lib/clamav/soc-custom-ioc.hsb /tmp/sample-dropper.bin
```

## Limites e trade-offs
Um erro de sintaxe em um arquivo `.ndb`, `.ldb` ou `.yar` customizado colocado em `/var/lib/clamav/` pode impedir a recarga do `clamd`; valide sempre qualquer regra nova com `clamscan -d <arquivo-regra>` antes de movê-la para produção.

## Como verificar
Execute `clamscan -d /var/lib/clamav/soc-custom-ioc.hsb /tmp/sample-dropper.bin` e confirme a detecção `UNOFFICIAL` com código de saída `1`.

## Conexões
- [[clamav-varredura-tempo-real-clamonacc-fanotify-on-access-linux]] — Veja também: ClamAV: Varredura On-Access em Tempo Real (`clamonacc`) via Linux `fanotify`.
- [[clamav-bytecode-signatures-bc-clambc-llvm-runtime-sandbox]] — Veja também: ClamAV: Assinaturas de Bytecode (`.cbc`), Sandbox Runtime e Depuração com `clambc`.
- [[clamav-arquitetura-libclamav-clamd-clamscan-freshclam]] — Referência cruzada direta com clamav-arquitetura-libclamav-clamd-clamscan-freshclam.
- [[clamav-atualizacao-freshclam-cvd-cld-private-local-mirrors]] — Referência cruzada direta com clamav-atualizacao-freshclam-cvd-cld-private-local-mirrors.

## Fontes
- [Cisco ClamAV Official Documentation — Usage Manual (libclamav Architecture, clamd, clamdscan, clamonacc, freshclam, sigtool & clambc)](https://raw.githubusercontent.com/Cisco-Talos/clamav/main/README.md) — Manual oficial de uso do ClamAV detalhando o fluxo de varredura cliente/servidor do clamd, utilitários de banco e configuração; consultado em 2026-10-03.
- [Cisco ClamAV GitHub — README.md (Open-Source Antivirus Engine Overview, Signatures, Packaging & Licensing)](https://docs.clamav.net/manual/Usage.html) — README oficial do Cisco-Talos/clamav descrevendo a arquitetura da engine, suporte multiplataforma e documentação de assinaturas; consultado em 2026-10-03.
- [Cisco ClamAV Official Documentation — Signature Writing Manual](https://docs.clamav.net/manual/Signatures.html) — Manual oficial de criação de assinaturas customizadas, lógicas, bytecode e YARA no ClamAV; consultado em 2026-10-03.
