---
id: software.seguranca.tranche04.000317
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

# ClamAV: Alertas Heurísticos, Bloqueio de Macros OLE2, Arquivos Criptografados e Prevenção de DLP

## Em uma frase
Além de assinaturas exatas de malware, a `libclamav` possui motores heurísticos configuráveis para detectar macros VBA em documentos Office (`AlertOLE2Macros`), arquivos ZIP/PDF protegidos por senha (`AlertEncrypted`) e padrões de vazamento de dados (`StructuredDataDetection`).

## Por que importa
Atacantes frequentemente enviam anexos `.zip` ou `.pdf` cifrados com a senha escrita no corpo do e-mail para cegar scanners antivírus; alertar ou reter arquivos criptografados fecha esse vetor de evasão.

## Como funciona
No `clamd.conf`, diretivas `HeuristicAlerts yes` e `AlertPhishingSSLMismatch yes` ativam detecções comportamentais com prefixo `Heuristics.*`, enquanto `AlertEncryptedArchive yes` e `AlertEncryptedDoc yes` sinalizam containers opacos como `Heuristics.Encrypted.Zip` ou `Heuristics.Encrypted.PDF`. O módulo DLP detecta números de cartão de crédito (validados por algoritmo de Luhn) e SSNs acima de uma contagem mínima (`StructuredMinCreditCardCount`).

## Exemplo
```ini
# /etc/clamav/clamd.conf — endurecimento heurístico para gateway de arquivos e e-mail
HeuristicAlerts yes
HeuristicScanPrecedence yes
AlertOLE2Macros yes
AlertEncrypted yes
AlertEncryptedArchive yes
AlertEncryptedDoc yes
AlertPhishingSSLMismatch yes
AlertPhishingCloak yes
```

## Limites e trade-offs
Ativar `AlertEncrypted yes` ou `AlertOLE2Macros yes` em diretórios de departamentos financeiros que trocam planilhas `.xlsm` legítimas ou relatórios bancários com senha exige tratamento diferenciado (quarentena para revisão em vez de deleção silenciosa).

## Como verificar
Teste `clamscan --alert-encrypted=yes arquivo-com-senha.zip` e confirme que o scanner emite `Heuristics.Encrypted.Zip FOUND` e retorna código de saída `1`.

## Conexões
- [[clamav-bytecode-signatures-bc-clambc-llvm-runtime-sandbox]] — Veja também: ClamAV: Assinaturas de Bytecode (`.cbc`), Sandbox Runtime e Depuração com `clambc`.
- [[clamav-integracao-pipelines-upload-api-milter-icap-s3]] — Veja também: ClamAV: Integração em Gateways de E-mail (`clamav-milter`), Servidores ICAP e Eventos S3/API.
- [[clamav-daemon-clamd-conf-unix-socket-tcp-instream-limites]] — Referência cruzada direta com clamav-daemon-clamd-conf-unix-socket-tcp-instream-limites.
- [[clamav-gerenciamento-falsos-positivos-ign2-fp-clamsubmit]] — Referência cruzada direta com clamav-gerenciamento-falsos-positivos-ign2-fp-clamsubmit.

## Fontes
- [Cisco ClamAV Official Documentation — Usage Manual (libclamav Architecture, clamd, clamdscan, clamonacc, freshclam, sigtool & clambc)](https://raw.githubusercontent.com/Cisco-Talos/clamav/main/README.md) — Manual oficial de uso do ClamAV detalhando o fluxo de varredura cliente/servidor do clamd, utilitários de banco e configuração; consultado em 2026-10-03.
- [Cisco ClamAV GitHub — README.md (Open-Source Antivirus Engine Overview, Signatures, Packaging & Licensing)](https://docs.clamav.net/manual/Usage.html) — README oficial do Cisco-Talos/clamav descrevendo a arquitetura da engine, suporte multiplataforma e documentação de assinaturas; consultado em 2026-10-03.
- [Cisco ClamAV Official Documentation — Signature Writing Manual](https://docs.clamav.net/manual/Signatures.html) — Manual oficial de criação de assinaturas customizadas, lógicas, bytecode e YARA no ClamAV; consultado em 2026-10-03.
