---
id: software.seguranca.tranche03.000297
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
fontes: ["https://docs.velociraptor.app/docs/overview/", "https://raw.githubusercontent.com/Velocidex/velociraptor/master/README.md", "https://github.com/Velocidex/velociraptor"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Velociraptor Perícia Forense de Disco (`ntfs`, `raw_ntfs`, `$MFT`, `$UsnJrnl` e Análise de Imagens de Disco via `remapping`)

## Em uma frase
Um dos maiores diferenciais forenses do Velociraptor é sua arquitetura de **Filesystem Accessors (`auto`, `file`, `ntfs`, `raw_ntfs`, `lazy_ntfs`, `zip`, `vss`, `ext4`)**: usando o accessor **`ntfs`** ou **`raw_ntfs`**, o Velociraptor lê a partição bruta (`\\.\C:`) fazendo bypass completo dos bloqueios de arquivo da API Win32 para extrair arquivos trancados pelo sistema operacional (como hives do Registry `SAM`/`SYSTEM`/`NTUSER.DAT`, `$MFT`, `$UsnJrnl:$J` e logs `.evtx` abertos)!

## Por que importa
Além disso, conforme documentado na seção *Interactive analysis* de `docs.velociraptor.app/docs/overview/`, se você recebeu uma imagem forense bruta de disco (`.dd`, `.raw`, `.vmdk`, `.ewf`/`.E01`) de uma máquina desligada, o Velociraptor permite criar uma regra de **`remapping`** e iniciar um **`virtual client`** que executa exatamente os mesmos artefatos VQL sobre a imagem de disco estática!

## Como funciona
Isso elimina a necessidade de manter duas ferramentas separadas (uma para triagem ao vivo em endpoints e outra para analisar imagens de disco em laboratório).

## Exemplo
```sql
-- Extraindo metadados diretamente da Master File Table ($MFT) via parser NTFS nativo do Velociraptor:
SELECT EntryNumber, OSPath, FileSize, Created0x10, Created0x30, LastModified0x10, SI_Lt_FN
FROM parse_mft(filename="C:/$MFT", accessor="ntfs")
WHERE OSPath =~ "(?i)\\\\Windows\\\\Temp\\\\.*\\.(exe|dll|ps1)$"
```

## Limites e trade-offs
Na consulta acima sobre `parse_mft()`, a coluna booleana **`SI_Lt_FN`** (*Standard Information timestamp < File Name timestamp*) detecta automaticamente a técnica antiforense de **Timestomping** (quando um malware altera a data de criação visível no Windows Explorer para parecer um arquivo antigo do sistema)!

## Como verificar
Teste os accessors disponíveis na CLI executando `velociraptor query "SELECT * FROM glob(globs='/*', accessor='file') LIMIT 5"`.

## Conexões
- [[velociraptor-monitoramento-tempo-real-client-events-etw-ebpf-sigma]] — Veja também: Velociraptor Detecção em Tempo Real (`CLIENT_EVENT`): monitoramento contínuo via `ETW` (Windows), `eBPF` (Linux) e regras `Sigma`.
- [[velociraptor-notebooks-interativos-pos-processamento-vql-timesketch-siem]] — Veja também: Velociraptor `Notebooks` Colaborativos e Exportação (`Timesketch`, `Splunk`, `Elastic` e `S3`): análise pós-coleta sem reinterrogar o host.

## Fontes
- [Velociraptor Official Documentation — Overview (Incident Response Timeline, VQL Engine, Client-Server/Offline/Virtual Modes, Monitoring & gRPC API)](https://docs.velociraptor.app/docs/overview/) — Visão geral oficial da documentação do Velociraptor explicando a atuação no passado/presente/futuro do incidente, modos de operação, VQL e ecossistema; consultado em 2026-10-03.
- [Velociraptor GitHub — README.md (Endpoint Visibility and Collection Tool, Quick Start, Build Collector, Artifact Exchange & Platforms)](https://raw.githubusercontent.com/Velocidex/velociraptor/master/README.md) — README oficial do Velocidex/velociraptor documentando execução da GUI, criação de coletores locais e o repositório comunitário Artifact Exchange; consultado em 2026-10-03.
- [Velociraptor — Official GitHub Repository (Velocidex / Rapid7)](https://github.com/Velocidex/velociraptor) — Repositório oficial open-source do Velociraptor; consultado em 2026-10-03.
