---
id: software.seguranca.tranche03.000204
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-03.md"
fontes: ["https://raw.githubusercontent.com/zeek/zeek/master/doc/about/architecture.rst", "https://raw.githubusercontent.com/zeek/zeek/master/README.md", "https://github.com/zeek/zeek"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Zeek File Analysis Framework (`FAF`): dissecção agnóstica de protocolo, detecção de MIME (`file_sniff`) e cálculo de hashes (`MD5`, `SHA1`, `SHA256`)

## Em uma frase
Conforme descrito em `doc/about/architecture.rst` (*"File analysis dissects the content of files transferred over sessions"*), o **File Analysis Framework (FAF)** do Zeek desacopla a análise do arquivo do protocolo de transporte: não importa se um executável Windows PE ou script malicioso foi transferido via **HTTP**, **SMB**, **FTP**, **SMTP** ou **IRC**, ele passa pelo mesmo pipeline de inspeção de arquivos e gera registros padronizados em `files.log`!

## Por que importa
Atacantes frequentemente renomeiam um executável `.exe` para `.jpg` ou o transferem por compartilhamento SMB interno; depender do nome da URL ou apenas de um proxy HTTP deixa passar transferências em outros protocolos.

## Como funciona
No evento **`file_sniff(f: fa_file, meta: fa_metadata)`**, o Zeek já identificou o **MIME type real** pelos *magic bytes* do conteúdo (ex.: `application/x-dosexec` ou `application/x-executable`), permitindo anexar dinamicamente analisadores de hash (`Files::add_analyzer(f, Files::ANALYZER_SHA256)`) e extrair uma cópia forense para o disco (`Files::ANALYZER_EXTRACT`)!

## Exemplo
```zeek
# Script extract-executables.zeek: calcula SHA-256 e extrai automaticamente binários PE/ELF detectados na rede:
event file_sniff(f: fa_file, meta: fa_metadata)
    {
    if ( ! meta?$mime_type )
        return;

    if ( meta$mime_type == "application/x-dosexec" || meta$mime_type == "application/x-executable" )
        {
        Files::add_analyzer(f, Files::ANALYZER_SHA256);
        local ext_file = fmt("extracted-%s.bin", f$id);
        Files::add_analyzer(f, Files::ANALYZER_EXTRACT, [$extract_filename=ext_file]);
        }
    }
```

## Limites e trade-offs
Defina um limite máximo de tamanho de arquivo extraído (`FileExtract::default_limit`) e monitore o espaço em disco da pasta `extract_files/` para evitar preenchimento de disco por transferências legítimas de imagens ISO.

## Como verificar
Teste com `zeek -C -r http-download.pcap ./extract-executables.zeek` e confira a coluna `sha256` e `extracted` em `files.log`.

## Conexões
- [[zeeknsm-linguagem-scripts-eventos-tipos-nativos-addr-subnet-port-table]] — Veja também: Zeek Scripting Language: programação orientada a eventos com tipos nativos de rede (`addr`, `subnet`, `port`, `interval`, `set` e `table`).
- [[zeeknsm-notice-framework-alertas-notice-log-action-alarm-hook]] — Veja também: Zeek Notice Framework (`notice.log`): geração de alertas contextuais (`NOTICE`), deduplicação por `suppress_for` e hooks de resposta.

## Fontes
- [Zeek GitHub — README.md (Network Traffic Analysis & Security Monitoring Framework, Key Features, Scripting & Tooling)](https://raw.githubusercontent.com/zeek/zeek/master/doc/about/architecture.rst) — README oficial do zeek/zeek apresentando o framework de análise semântica de rede, estado de camada de aplicação e linguagem de scripts; consultado em 2026-10-03.
- [Zeek Official Documentation — Architecture (doc/about/architecture.rst: Event Engine, Packet/Session/File Analysis & Script Interpreter)](https://raw.githubusercontent.com/zeek/zeek/master/README.md) — Documentação oficial de arquitetura do Zeek detalhando a separação entre o Event Engine neutro de política e o Script Interpreter; consultado em 2026-10-03.
- [Zeek Network Security Monitor — Official GitHub Repository](https://github.com/zeek/zeek) — Repositório oficial BSD-3-Clause do Zeek; consultado em 2026-10-03.
