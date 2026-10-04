---
id: software.seguranca.tranche04.000320
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

# ClamAV: Supressão Auditável de Falsos Positivos (`.ign2` e `.fp`) e Submissão com `clamsubmit`

## Em uma frase
O ClamAV permite suprimir falsos positivos de forma controlada através de listas de exclusão por hash SHA-256 do arquivo confiável (`.fp` / `.sfp`) ou pelo nome exato da assinatura problemática (`.ign2`).

## Por que importa
Desligar todo o scanner antivírus em um pipeline porque um único pacote interno ou instalador legítimo disparou uma assinatura heurística expõe toda a aplicação; o arquivo `.fp` permite liberar exclusivamente aquele artefato imutável.

## Como funciona
Criar um arquivo `local-whitelist.fp` (ou `.hsb` com extensão `.fp`) em `/var/lib/clamav/` contendo `hash:tamanho:nome` instrui a `libclamav` a declarar limpa apenas aquela sequência exata de bytes. Já um arquivo `local.ign2` contendo o nome da assinatura (ex.: `Win.Trojan.Generic-12345`) desativa aquela regra específica globalmente enquanto o falso positivo é reportado à equipe Cisco Talos via `clamsubmit`.

## Exemplo
```bash
# Gerar entrada .fp baseada em hash para liberar apenas um binário interno específico
sigtool --sha256 /opt/releases/internal-installer.exe > /var/lib/clamav/internal-whitelist.fp

# Recarregar o banco de dados do clamd sem reiniciar o daemon
clamdscan --reload
```

## Limites e trade-offs
Usar `.ign2` para silenciar assinaturas genéricas amplas desprotege todos os usuários contra aquela família de malware; prefira sempre `.fp` por hash SHA-256 do arquivo falso positivo específico.

## Como verificar
Execute `clamdscan /opt/releases/internal-installer.exe` após `clamdscan --reload` e confirme que o arquivo passa com status `OK` enquanto outros testes continuam sendo detectados.

## Conexões
- [[clamav-monitoramento-performance-clamdtop-filas-threads-memoria]] — Veja também: ClamAV: Monitoramento Operacional com `clamdtop`, Pool de Memória e Dimensionamento em Containers.
- [[clamav-assinaturas-customizadas-hdb-ndb-ldb-yara-sigtool]] — Referência cruzada direta com clamav-assinaturas-customizadas-hdb-ndb-ldb-yara-sigtool.
- [[clamav-heuristicas-dlp-macros-ole2-pdf-encrypted-archives]] — Referência cruzada direta com clamav-heuristicas-dlp-macros-ole2-pdf-encrypted-archives.
- [[clamav-arquitetura-libclamav-clamd-clamscan-freshclam]] — Referência cruzada direta com clamav-arquitetura-libclamav-clamd-clamscan-freshclam.

## Fontes
- [Cisco ClamAV Official Documentation — Usage Manual (libclamav Architecture, clamd, clamdscan, clamonacc, freshclam, sigtool & clambc)](https://raw.githubusercontent.com/Cisco-Talos/clamav/main/README.md) — Manual oficial de uso do ClamAV detalhando o fluxo de varredura cliente/servidor do clamd, utilitários de banco e configuração; consultado em 2026-10-03.
- [Cisco ClamAV GitHub — README.md (Open-Source Antivirus Engine Overview, Signatures, Packaging & Licensing)](https://docs.clamav.net/manual/Usage.html) — README oficial do Cisco-Talos/clamav descrevendo a arquitetura da engine, suporte multiplataforma e documentação de assinaturas; consultado em 2026-10-03.
- [Cisco ClamAV Official Documentation — Signature Writing Manual](https://docs.clamav.net/manual/Signatures.html) — Manual oficial de criação de assinaturas customizadas, lógicas, bytecode e YARA no ClamAV; consultado em 2026-10-03.
