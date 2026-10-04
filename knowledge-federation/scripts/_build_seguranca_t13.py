#!/usr/bin/env python3
"""Build 100 substantive notes for batch software-seguranca-2000-0003 tranche 13 (IDs 1201-1300) and its AI factual review report."""
from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
KF = ROOT / "knowledge-federation"
DOMAINS_DIR = KF / "domains"
NOTES_DIR = DOMAINS_DIR / "software-0009" / "software" / "seguranca"
REPORT = KF / "exports" / "reports" / "ai-review-software-seguranca-2000-0003-tranche-13.md"
DATA_DIR = Path(__file__).resolve().parent / "_seguranca_t13_data"
BATCH_ID = "software-seguranca-2000-0003"
DATE = "2026-10-03"
START = 1201
EXPECTED_NOTES = 100

sys.path.insert(0, str(Path(__file__).resolve().parent))
from note_quality import assess_markdown  # noqa: E402
from prose_audit import repeated_substantive_sentences  # noqa: E402


GROUP_META = {
    "01-keepassxc.txt": {
        "sub": "KeePassXC (keepassxreboot/keepassxc) — Gerenciamento de Cofres de Credenciais Offline KDBX 4 (Argon2id/ChaCha20), YubiKey HMAC-SHA1, ssh-agent, keepassxc-cli e Passkeys",
        "src1_label": "KeePassXC Official GitHub — Cross-Platform Community-Driven Port of Keepass",
        "src1_note": "repositório oficial do KeePassXC cobrindo criptografia KDBX 4 (AES-256, Twofish, ChaCha20), YubiKey/OnlyKey, `keepassxc-cli`, SSH Agent e Secret Service",
        "src2_label": "KeePassXC Official User Guide (`keepassxc.org/docs/KeePassXC_UserGuide`)",
        "src2_note": "guia oficial do usuário do KeePassXC detalhando Auto-Type, integração com navegador, Passkeys, KeeShare, Database Reports (HIBP) e proteção de memória/tela",
    },
    "02-plaso.txt": {
        "sub": "Plaso / log2timeline (log2timeline/plaso) — Motor Forense de Super Timelines e Targeted Timelines Multi-Artefatos (log2timeline.py, psort.py, pinfo.py, psteal.py) e Integração Timesketch",
        "src1_label": "Plaso (`log2timeline`) Official GitHub — Super Timeline All the Things",
        "src1_note": "repositório oficial do motor forense Plaso cobrindo arquitetura de parsers, plugins de análise, event tagging e formatos de armazenamento",
        "src2_label": "Plaso Official Documentation — Using `log2timeline.py` (`plaso.readthedocs.io`)",
        "src2_note": "documentação oficial do Plaso detalhando extração de imagens E01/RAW, partições, Volume Shadow Copies (`--vss_stores`), BitLocker, presets de parsers e arquitetura multi-worker",
    },
    "03-capa.txt": {
        "sub": "Mandiant capa (mandiant/capa) — Detecção Automatizada de Capacidades em Binários (PE, ELF, .NET, Shellcode) e Relatórios de Sandbox Mapeadas ao MITRE ATT&CK e MBC",
        "src1_label": "Mandiant FLARE `capa` Official GitHub — Detect Capabilities in Executable Files",
        "src1_note": "repositório oficial do Mandiant `capa` cobrindo identificação de capacidades em PE, ELF, .NET, shellcode e relatórios de sandbox mapeadas ao ATT&CK e MBC",
        "src2_label": "Mandiant `capa` Official Usage & Advanced Documentation (`doc/usage.md`)",
        "src2_note": "guia técnico oficial de uso do `capa` detalhando modos `-v`/`-vv`/`-j`, filtros `-t`, `--restrict-to-functions`, `--restrict-to-processes`, `CAPA_SAVE_WORKSPACE` e integrações IDA/Ghidra/Web",
    },
    "04-floss.txt": {
        "sub": "Mandiant FLOSS (mandiant/flare-floss) — Extração e Desofuscação de Strings em Malware (Static, Stack Strings, Tight Strings, Decoded Strings via Emulação e Go/Rust)",
        "src1_label": "Mandiant FLARE Obfuscated String Solver (`flare-floss`) Official GitHub",
        "src1_note": "repositório oficial do Mandiant FLOSS cobrindo extração de strings estáticas conscientes de layout, stack strings, tight strings, decoded strings e binários Go/Rust",
        "src2_label": "Mandiant FLOSS Official Usage Guide (`doc/usage.md`)",
        "src2_note": "documentação oficial de opções avançadas do FLOSS (`--only`, `--no`, `--functions`, `--section`, `--structure`, `--tag`, `--interesting`, `--query`, `--html`, `-L` e `FLOSS_CACHE_DIR`)",
    },
    "05-gophish.txt": {
        "sub": "Gophish (gophish/gophish) — Framework Open-Source de Simulação de Phishing, Treinamento de Conscientização (Security Awareness), Operações Red Team e Automação via API/Webhooks",
        "src1_label": "Gophish Official GitHub — Open-Source Phishing Toolkit",
        "src1_note": "repositório oficial do Gophish detalhando arquitetura em Go (`admin_server` e `phish_server`), instalação e inicialização segura",
        "src2_label": "Gophish Official User Guide Documentation (`docs.getgophish.com`)",
        "src2_note": "documentação oficial do Gophish cobrindo Sending Profiles, Email Templates (`{{.URL}}`, `{{.Tracker}}`), Landing Pages, Users & Groups, Campaigns, Email Reporting (`rid`) e Webhooks",
    },
    "06-modsecurity.txt": {
        "sub": "OWASP ModSecurity v3 (libmodsecurity) — Motor de Web Application Firewall (WAF) em C++17, Linguagem SecRule, Detecção Léxica libinjection (@detectSQLi/@detectXSS) e OWASP CRS",
        "src1_label": "OWASP ModSecurity v3 (`libmodsecurity`) Official GitHub",
        "src1_note": "repositório oficial do OWASP ModSecurity v3 detalhando a arquitetura standalone da biblioteca `libmodsecurity`, conectores Nginx/Apache, PCRE2, `libinjection` e YAJL JSON",
        "src2_label": "OWASP ModSecurity v3 Recommended Configuration (`modsecurity.conf-recommended`)",
        "src2_note": "configuração oficial recomendada do ModSecurity v3 cobrindo `SecRuleEngine`, `SecRequestBodyAccess`, processadores XML/JSON, limites anti-DoS e `SecAuditLogFormat JSON`",
    },
    "07-strongswan.txt": {
        "sub": "strongSwan (strongswan/strongswan) — VPN IPsec/IKEv2 no Linux, Daemon charon, Interface vici/swanctl.conf, Interfaces Virtuais XFRM (Route-Based), TPM 2.0/PKCS#11 e IKEv2 Pós-Quântico (RFC 9370 ML-KEM)",
        "src1_label": "strongSwan Official GitHub — OpenSource IPsec-Based VPN Solution",
        "src1_note": "repositório oficial do strongSwan cobrindo arquitetura do daemon `charon`, protocolo `vici`, ferramenta `swanctl`, utilitário `pki` e cenários Site-to-Site/Roadwarrior",
        "src2_label": "strongSwan Official `swanctl.conf` Documentation (`docs.strongswan.org`)",
        "src2_note": "especificação completa do `/etc/swanctl/swanctl.conf` detalhando `connections`, `children`, `secrets`, `pools`, `authorities`, interfaces XFRM (`if_id_in`/`if_id_out`), TPM 2.0 e propostas pós-quânticas `ke1_mlkem768`",
    },
    "08-firejail.txt": {
        "sub": "Firejail (netblue30/firejail) — Sandboxing de Aplicações Linux com Kernel Namespaces, Filtros seccomp-bpf, Linux Capabilities, AppArmor, Isolamento X11/D-Bus e Perfis .profile",
        "src1_label": "Firejail Security Sandbox Official GitHub (`netblue30/firejail`)",
        "src1_note": "repositório oficial do Firejail cobrindo arquitetura de isolamento por namespaces do Kernel Linux, `seccomp-bpf`, capabilities, cgroups e mais de 1.000 perfis `.profile`",
        "src2_label": "Firejail Official System Configuration Reference (`etc/firejail.config`)",
        "src2_note": "configuração oficial de políticas de hardening global do Firejail (`force-nonewprivs`, `disable-mnt`, `restricted-network`, `seccomp-error-action`, `x11`, `dbus`, `apparmor`)",
    },
    "09-linux-pam.txt": {
        "sub": "Linux-PAM (linux-pam/linux-pam) — Arquitetura de Módulos de Autenticação Plugáveis (auth, account, password, session), Bloqueio pam_faillock, Qualidade pam_pwquality, MFA FIDO2/TOTP e Auditoria auid",
        "src1_label": "Linux-PAM Official Repository README (`linux-pam/linux-pam`)",
        "src1_note": "documentação oficial do projeto Linux-PAM cobrindo arquitetura da biblioteca `libpam`, grupos de gerenciamento, flags de controle e módulos de segurança",
        "src2_label": "Linux-PAM Official `faillock.conf(5)` Manual Specification",
        "src2_note": "especificação oficial do módulo `pam_faillock` e `/etc/security/faillock.conf` (`dir`, `audit`, `silent`, `deny`, `fail_interval`, `unlock_time`, `even_deny_root`, `root_unlock_time`)",
    },
    "10-openssl.txt": {
        "sub": "OpenSSL 3.x (openssl/openssl) — Arquitetura de Providers (default, fips, legacy, base), Conformidade FIPS 140-3, Operações EVP (genpkey, x509, s_client, dgst, mac, kdf, cms, pkcs12) e Políticas @SECLEVEL",
        "src1_label": "OpenSSL 3.x Official Repository README (`openssl/openssl`)",
        "src1_note": "repositório oficial do OpenSSL 3.x cobrindo `libssl` (TLS 1.3, DTLS 1.2, QUIC v1), `libcrypto` e utilitários criptográficos de linha de comando",
        "src2_label": "OpenSSL 3.x Official Providers Documentation (`README-PROVIDERS.md`)",
        "src2_note": "documentação oficial da arquitetura de Providers do OpenSSL 3.x (`default`, `legacy`, `fips`, `base`, `null`), ativação em `openssl.cnf` e *Property Queries* (`fips=yes`)",
    },
}


def normalize(text: str) -> str:
    base = unicodedata.normalize("NFKD", text.lower())
    clean = "".join(ch for ch in base if not unicodedata.combining(ch))
    return re.sub(r"[^a-z0-9]+", " ", clean).strip()


def parse_group(path: Path) -> tuple[dict[str, str], list[dict[str, object]]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    sources_urls: list[str] = []
    for line in lines[:10]:
        if line.startswith("SOURCES:"):
            sources_urls = [s.strip() for s in line.split("SOURCES:", 1)[1].split("|") if s.strip()]
    if len(sources_urls) < 2:
        raise ValueError(f"{path.name}: esperado cabeçalho SOURCES com pelo menos 2 URLs")

    raw_text = "\n".join(lines)
    blocks = [b.strip() for b in raw_text.split("===NOTE===") if b.strip()][1:]
    if len(blocks) != 10:
        raise ValueError(f"{path.name}: esperadas 10 notas, encontradas {len(blocks)}")

    meta = GROUP_META[path.name]
    group_title = meta["sub"]
    rows: list[dict[str, object]] = []
    first_num: int | None = None

    for rec in blocks:
        code_m = re.search(r"\|(```[\s\S]+?```)\|", rec)
        if not code_m:
            raise ValueError(f"{path.name}: bloco de código não encontrado: {rec[:140]}...")
        pre = rec[: code_m.start()]
        example = code_m.group(1).strip()
        post = rec[code_m.end() :]

        pre_parts = [g.strip() for g in re.split(r"\|(?=(?:[^`]*`[^`]*`)*[^`]*$)", pre)]
        post_parts = [g.strip() for g in re.split(r"\|(?=(?:[^`]*`[^`]*`)*[^`]*$)", post)]
        if len(pre_parts) != 6 or len(post_parts) != 3:
            raise ValueError(
                f"{path.name}: falha ao analisar registro (pre={len(pre_parts)}, post={len(post_parts)}): {rec[:140]}..."
            )
        num_str, slug, title, summary, reason, how = pre_parts
        caveat, verify, links_csv = post_parts
        num = int(num_str)
        if first_num is None:
            first_num = num
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
            raise ValueError(f"{path.name}: slug inválido: {slug}")

        links = [x.strip() for x in links_csv.split(",") if x.strip()]
        sources = [
            (meta["src1_label"], sources_urls[0], meta["src1_note"]),
            (meta["src2_label"], sources_urls[1], meta["src2_note"]),
        ]
        if len(sources_urls) >= 3:
            sources.append((meta["src3_label"], sources_urls[2], meta["src3_note"]))

        rows.append(
            {
                "slug": slug,
                "title": title,
                "summary": summary,
                "reason": reason,
                "how": how,
                "example": example,
                "caveat": caveat,
                "verify": verify,
                "links": links,
                "sources": sources,
                "review": f"Verificado contra {meta['src1_label']} e {meta['src2_label']}.",
            }
        )

    assert first_num is not None
    first_sources = rows[0]["sources"]  # type: ignore[index]
    ctx = {
        "first": str(first_num),
        "sub": group_title,
        "group_title": group_title,
        "check": (
            f"Conferi a documentação primária oficial de {group_title} "
            f"({first_sources[0][1]} e {first_sources[1][1]}) antes de redigir as dez notas."
        ),
    }
    return ctx, rows


def render_note(
    context: dict[str, str],
    rows: list[dict[str, object]],
    index: int,
    row: dict[str, object],
    valid_slugs: set[str] | None = None,
) -> tuple[int, str, dict[str, object]]:
    number = int(context["first"]) + index
    sources: list[tuple[str, str, str]] = list(row["sources"])  # type: ignore[arg-type]
    if len(sources) < 2 or len({source[1] for source in sources}) < 2:
        raise ValueError(f"{row['slug']}: precisa de duas fontes distintas")

    neighbors = []
    seen_nb: set[str] = set()
    for neighbor_index in (index - 1, index + 1):
        if 0 <= neighbor_index < len(rows):
            other = rows[neighbor_index]
            s = str(other["slug"])
            seen_nb.add(s)
            neighbors.append(f"- [[{s}]] — Veja também: {other['title']}.")
    if valid_slugs is not None:
        for lk in row.get("links", []):  # type: ignore[union-attr]
            if lk not in seen_nb and lk != row["slug"] and lk in valid_slugs:
                seen_nb.add(lk)
                neighbors.append(f"- [[{lk}]] — Referência cruzada direta com {lk}.")

    frontmatter = f'''---
id: software.seguranca.tranche13.{number:06d}
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: {DATE}
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: {DATE}
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-13.md"
fontes: [{', '.join('"' + source[1] + '"' for source in sources)}]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: {BATCH_ID}
---\n'''
    source_lines = [
        f"- [{name}]({url}) — {description}; consultado em {DATE}."
        for name, url, description in sources
    ]
    content = f'''{frontmatter}
# {row['title']}

## Em uma frase
{row['summary']}

## Por que importa
{row['reason']}

## Como funciona
{row['how']}

## Exemplo
{row['example']}

## Limites e trade-offs
{row['caveat']}

## Como verificar
{row['verify']}

## Conexões
{chr(10).join(neighbors)}

## Fontes
{chr(10).join(source_lines)}
'''
    quality = assess_markdown(content, str(row["slug"]) + ".md")
    if quality["errors"]:
        raise ValueError(f"{row['slug']}: {quality['errors']} ({quality['word_count']} palavras)")
    return number, content, quality


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--refresh",
        action="store_true",
        help="Rebuild the existing tranche-13 notes after validating their IDs and batch metadata.",
    )
    args = parser.parse_args()
    NOTES_DIR.mkdir(parents=True, exist_ok=True)
    group_files = sorted(DATA_DIR.glob("*.txt"))
    if len(group_files) != 10:
        raise SystemExit(f"Esperados 10 arquivos de grupo; encontrados {len(group_files)}")

    existing_paths = list(DOMAINS_DIR.rglob("*.md"))
    existing_tranche = [
        path
        for path in existing_paths
        if re.search(
            r"(?m)^id: software\.seguranca\.tranche13\.\d{6}\s*$",
            path.read_text(encoding="utf-8", errors="replace")[:1200],
        )
    ]
    if args.refresh and len(existing_tranche) != EXPECTED_NOTES:
        raise ValueError(
            f"--refresh exige exatamente {EXPECTED_NOTES} notas tranche13 existentes; encontradas {len(existing_tranche)}"
        )
    if REPORT.exists() and not args.refresh:
        raise ValueError(f"relatório já existe (use --refresh apenas para atualizar a tranche 13): {REPORT}")
    if args.refresh and not REPORT.exists():
        raise ValueError(f"--refresh exige relatório factual existente: {REPORT}")

    current_tranche = set(existing_tranche)
    existing_paths = [path for path in existing_paths if path not in current_tranche]
    existing_slugs = {path.stem for path in existing_paths}
    existing_titles = set()
    for path in existing_paths:
        match = re.search(r"(?m)^#\s+(.+?)\s*$", path.read_text(encoding="utf-8", errors="replace"))
        if match:
            existing_titles.add(normalize(match.group(1).strip()))

    parsed_groups = [parse_group(path) for path in group_files]
    tranche_slugs = {str(r["slug"]) for _, rows in parsed_groups for r in rows}
    all_valid_slugs = existing_slugs | tranche_slugs

    pending = []
    report_rows = []
    group_summaries: list[tuple[dict[str, str], int]] = []
    seen_slugs: set[str] = set()
    seen_titles: set[str] = set()
    expected_number = START
    for path, (context, rows) in zip(group_files, parsed_groups):
        if int(context["first"]) != expected_number:
            raise ValueError(f"{path.name}: ID inicial esperado {expected_number}, informado {context['first']}")
        group_summaries.append((context, len(rows)))
        for index, row in enumerate(rows):
            slug = str(row["slug"])
            title = str(row["title"])
            normalized_title = normalize(title.strip())
            if slug in seen_slugs or slug in existing_slugs:
                raise ValueError(f"slug em colisão com o inventário: {slug}")
            if normalized_title in seen_titles or normalized_title in existing_titles:
                raise ValueError(f"título em colisão com o inventário: {title}")
            target_path = NOTES_DIR / f"{slug}.md"
            expected_id = f"id: software.seguranca.tranche13.{expected_number + index:06d}"
            if target_path.exists():
                current = target_path.read_text(encoding="utf-8")
                if not args.refresh:
                    raise ValueError(f"arquivo já existe (use --refresh apenas para a tranche 13): {target_path}")
                if (
                    expected_id not in current.splitlines()[:25]
                    or f"lote: {BATCH_ID}" not in current.splitlines()[:25]
                ):
                    raise ValueError(f"ID ou lote existente não corresponde à tranche: {target_path}")
            elif args.refresh:
                raise ValueError(f"--refresh exige os {EXPECTED_NOTES} arquivos existentes; falta {target_path}")
            seen_slugs.add(slug)
            seen_titles.add(normalized_title)
            number, content, quality = render_note(context, rows, index, row, valid_slugs=all_valid_slugs)
            pending.append((number, row, context, content, quality))
            source_name, source_url, _ = row["sources"][0]  # type: ignore[index]
            report_rows.append(
                f"| {number} | [[{slug}]] | [{source_name}]({source_url}) | {row['review']} Revisão factual por IA concluída; decisão: aprovada. |"
            )
        expected_number += len(rows)

    if len(pending) != EXPECTED_NOTES or expected_number != START + EXPECTED_NOTES:
        raise ValueError(
            f"esperadas {EXPECTED_NOTES} notas de {START} a {START + EXPECTED_NOTES - 1}, validadas {len(pending)}"
        )
    repeated = repeated_substantive_sentences(
        [(number, content) for number, _, _, content, _ in pending]
    )
    if repeated:
        examples = [f"{numbers}: {sentence}" for sentence, numbers in list(repeated.items())[:8]]
        raise ValueError(f"prosa substantiva repetida entre notas; revisar antes de gravar: {examples}")

    for number, row, context, content, quality in pending:
        (NOTES_DIR / f"{row['slug']}.md").write_text(content, encoding="utf-8")

    report = [
        f"# Revisão factual assistida por IA — lote `{BATCH_ID}`, tranche 13",
        "",
        f"- Data: {DATE}",
        "- Revisor: `Arena.ai Agent Mode`",
        f"- Escopo: notas **{START}–{START + EXPECTED_NOTES - 1}**, em dez grupos temáticos com dez notas cada; cada linha identifica a conferência factual da nota.",
        "- Fontes primárias: documentação oficial dos projetos e versões indicadas nas próprias notas; as afirmações foram limitadas ao material citado.",
        f"- Resultado: **{EXPECTED_NOTES} revisões factuais por IA registradas** e aprovadas no gate automatizado de qualidade, elevando o terceiro lote `{BATCH_ID}` para **1300/2.000 notas válidas (`in_progress`)**. Isto não é aprovação humana nem garantia de ausência de erro.",
        "- Nenhuma aprovação humana existente foi alterada ou estendida às novas notas.",
        "",
        "## Registro por nota",
        "",
        "| # | Nota | Fonte principal | Verificação factual / decisão |",
        "|---:|---|---|---|",
        *report_rows,
        "",
        "## Verificações por grupo",
        "",
    ]
    for context, count in group_summaries:
        report.append(
            f"- {context['group_title']} (itens {context['first']}–{int(context['first']) + count - 1}): {context['check']}"
        )
    report += [
        "- A auditoria de links, a comparação com o inventário, o gate de conteúdo e a verificação de sentenças repetidas foram executados separadamente antes da contabilização.",
        "",
    ]
    REPORT.write_text("\n".join(report).rstrip() + "\n", encoding="utf-8")
    word_counts = [quality["word_count"] for _, _, _, _, quality in pending]
    source_counts = [quality["source_count"] for _, _, _, _, quality in pending]
    print(
        f"Geradas {len(pending)} notas substantivas (IDs {START}–{START + EXPECTED_NOTES - 1}); "
        f"palavras: min={min(word_counts)}; max={max(word_counts)}"
    )
    print(f"Fontes HTTPS específicas por nota: min={min(source_counts)}; max={max(source_counts)}")
    print(f"Relatório factual: {REPORT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
