---
id: software.seguranca.tranche04.000316
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

# ClamAV: Assinaturas de Bytecode (`.cbc`), Sandbox Runtime e Depuração com `clambc`

## Em uma frase
Assinaturas de Bytecode (`.cbc`) do ClamAV são programas restritos escritos em um dialeto C seguro, compilados para bytecode LLVM e executados em uma máquina virtual/JIT isolada dentro da `libclamav`.

## Por que importa
Permitem implementar desempacotadores (*unpackers*) complexos, decodificadores de ofuscação aritmética e verificações estruturais de cabeçalhos PE/PDF que são impossíveis de expressar apenas com regex ou padrões `.ldb`.

## Como funciona
O motor de bytecode impõe limites estritos de segurança: ausência de chamadas de sistema arbitrárias, acesso de memória restrito aos buffers do arquivo inspecionado e *timeout* rigoroso em milissegundos (`BytecodeTimeout` no `clamd.conf`). O utilitário `clambc` inspeciona os metadados, o código intermediário e executa testes isolados de arquivos `.cbc`.

## Exemplo
```bash
# Extrair e inspecionar assinaturas .cbc do banco oficial bytecode.cvd
mkdir -p /tmp/clam-bc && cd /tmp/clam-bc
sigtool --unpack /var/lib/clamav/bytecode.cvd
clambc --info /tmp/clam-bc/Polite.cbc
```

## Limites e trade-offs
Por motivos de segurança (`BytecodeSecurity TrustSigned` por padrão), o `clamd` só carrega bytecodes `.cbc` assinados digitalmente pela equipe Cisco Talos, a menos que `--bytecode-unsigned=yes` seja explicitamente habilitado em ambientes de laboratório.

## Como verificar
Execute `clamconf | grep -i bytecode` e confirme que `Bytecode = "yes"` e `BytecodeSecurity = "TrustSigned"` estão ativos no daemon de produção.

## Conexões
- [[clamav-assinaturas-customizadas-hdb-ndb-ldb-yara-sigtool]] — Veja também: ClamAV: Escrita de Assinaturas Customizadas (`.hdb`, `.hsb`, `.ndb`, `.ldb`, `.yar`) e `sigtool`.
- [[clamav-heuristicas-dlp-macros-ole2-pdf-encrypted-archives]] — Veja também: ClamAV: Alertas Heurísticos, Bloqueio de Macros OLE2, Arquivos Criptografados e Prevenção de DLP.
- [[clamav-arquitetura-libclamav-clamd-clamscan-freshclam]] — Referência cruzada direta com clamav-arquitetura-libclamav-clamd-clamscan-freshclam.
- [[clamav-daemon-clamd-conf-unix-socket-tcp-instream-limites]] — Referência cruzada direta com clamav-daemon-clamd-conf-unix-socket-tcp-instream-limites.

## Fontes
- [Cisco ClamAV Official Documentation — Usage Manual (libclamav Architecture, clamd, clamdscan, clamonacc, freshclam, sigtool & clambc)](https://raw.githubusercontent.com/Cisco-Talos/clamav/main/README.md) — Manual oficial de uso do ClamAV detalhando o fluxo de varredura cliente/servidor do clamd, utilitários de banco e configuração; consultado em 2026-10-03.
- [Cisco ClamAV GitHub — README.md (Open-Source Antivirus Engine Overview, Signatures, Packaging & Licensing)](https://docs.clamav.net/manual/Usage.html) — README oficial do Cisco-Talos/clamav descrevendo a arquitetura da engine, suporte multiplataforma e documentação de assinaturas; consultado em 2026-10-03.
- [Cisco ClamAV Official Documentation — Signature Writing Manual](https://docs.clamav.net/manual/Signatures.html) — Manual oficial de criação de assinaturas customizadas, lógicas, bytecode e YARA no ClamAV; consultado em 2026-10-03.
