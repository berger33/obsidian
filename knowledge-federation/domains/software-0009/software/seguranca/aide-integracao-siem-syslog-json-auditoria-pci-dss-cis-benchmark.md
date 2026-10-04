---
id: software.seguranca.tranche12.001148
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-12.md"
fontes: ["https://raw.githubusercontent.com/aide/aide/master/README", "https://aide.github.io/doc/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Integração do AIDE com **SIEM e Conformidade (`PCI-DSS 11.5` / `CIS Benchmarks`)**: Parseando Relatórios de Alteração e Alertando sobre Drift

## Em uma frase
Tanto o **PCI-DSS v4.0 (Requisito 11.5.2)** quanto os **CIS Benchmarks para Linux (Controle 1.3.1 / 1.3.2 — *Ensure AIDE is installed and filesystem integrity is regularly checked*)** exigem que uma ferramenta de verificação de integridade de arquivos seja executada pelo menos uma vez por semana (ou diariamente em ambientes de alta criticidade) e que qualquer alteração não autorizada em arquivos críticos de sistema gere um alerta imediato para a equipe de segurança!

## Por que importa
Nas versões modernas do AIDE (v0.18 e v0.19+), você pode ajustar o nível e o formato do relatório (`report_format`, `report_level`, `report_detailed_init`, `report_base16`, `report_quiet`) e direcionar a saída para múltiplos destinos simultâneos usando a diretiva **`report_url`** (`report_url=stdout`, `report_url=file:/var/log/aide/aide.log`, `report_url=syslog:LOG_AUTH`)!

## Como funciona
Ao enviar o resumo para o **`syslog:LOG_AUTH`** (ou capturar o relatório detalhado em `/var/log/aide/aide.log` via agente **Wazuh**, **Filebeat** ou **Vector**), qualquer retorno diferente de `0` no `aide --check` abre automaticamente um incidente de **Drift de Integridade / Possível Comprometimento de Host** no SOC!

## Exemplo
```ini
# Configurar multiplas saidas de relatorio no aide.conf incluindo arquivo de auditoria local e canal Syslog LOG_AUTH para o SIEM
report_url=file:/var/log/aide/aide-check.log
report_url=syslog:LOG_AUTH
report_level=added_removed_entries
report_base16=yes
```

## Limites e trade-offs
A diretiva **`report_base16=yes`** instrui o AIDE a imprimir os hashes (`SHA-256`, `SHA-512`) no relatório em formato **hexadecimal padrão** (em vez de Base64 tradicional do AIDE), permitindo que o analista do SOC copie o hash do arquivo modificado diretamente do alerta do AIDE e o consulte no **VirusTotal** ou no **MISP** sem precisar convertê-lo!

## Como verificar
Vincule os alertas do AIDE no seu SIEM ao registro de execuções do Ansible/Puppet/Chef para classificar automaticamente mudanças causadas por deploys aprovados versus alterações fora de janela.

## Conexões
- [[aide-configuracao-modular-debian-ubuntu-aide-conf-d-update-aide-conf]] — Veja também: Arquitetura Modular no Debian/Ubuntu (**`/etc/aide/aide.conf.d/`**): **`update-aide.conf`**, **`aideinit`** e Integração com Pacotes `.deb`.
- [[aide-otimizacao-performance-workers-multithread-limites-io-producao]] — Veja também: Otimização de Performance e Controle de Impacto de I/O do AIDE em Produção: **Multithreading (`num_workers`)**, `ionice` e `nice`.
- [[aide-arquitetura-monitoramento-integridade-arquivos-fim-linux]] — Referência cruzada direta com aide-arquitetura-monitoramento-integridade-arquivos-fim-linux.
- [[aide-ciclo-operacional-init-check-update-codigos-retorno]] — Referência cruzada direta com aide-ciclo-operacional-init-check-update-codigos-retorno.
- [[atomicredteam-testes-linux-macos-containers-bash-sh-validacao-edr]] — Referência cruzada direta com atomicredteam-testes-linux-macos-containers-bash-sh-validacao-edr.

## Fontes
- [AIDE Official Repository README — Advanced Intrusion Detection Environment (v0.19)](https://raw.githubusercontent.com/aide/aide/master/README) — documentação oficial do código-fonte do AIDE cobrindo arquitetura, verificação criptográfica GPG, PCRE2 e bibliotecas `libnettle`/`libgcrypt`; consultado em 2026-10-03.
- [The Official AIDE Manual (`aide.github.io/doc`)](https://aide.github.io/doc/) — manual técnico oficial do AIDE detalhando regras de atributos (`p`, `i`, `n`, `u`, `g`, `s`, `m`, `c`, `S`, `acl`, `selinux`, `xattrs`, `e2fsattrs`, `sha256`, `sha512`), seleções regex e assinatura de banco de dados; consultado em 2026-10-03.
